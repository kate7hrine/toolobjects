from App.Server import Server
from App.Objects.Requirements.Requirement import Requirement
from Data.Types.JSON import JSON
from App.ACL.Tokens.Get import Get as TokensGet
from App.Storage.VirtualPath.Navigate import Navigate
from App import app
import aiohttp
import aiohttp_jinja2
import jinja2

class Client(Server):
    def _before_run(self, i):
        _templates = str(app.app.src.joinpath('assets').joinpath('client').joinpath('templates'))
        aiohttp_jinja2.setup(self._app, 
                             loader=jinja2.FileSystemLoader(_templates),
                             auto_reload = True)

    @classmethod
    def _requirements(cls) -> list:
        return [
            Requirement(
                name = 'Jinja2'
            ),
            Requirement(
                name = 'aiohttp-jinja2'
            )
        ]

    def _get_tokens(self, request):
        users = list()

        try:
            _json = JSON.fromText(request.cookies.get('tokens'))
            users = _json.data
        except Exception as e:
            self.log_error(e)

        return users

    def _get_template_context(self, request):
        return {
            'app_name': self.getOption('app.name'),
            'user': self._get_current_user(request)
        }

    def _auth(self, args: dict, request):
        args['auth'] = self._get_current_user(request)

        if args.get('auth') != None:
            self.log('auth as {0}'.format(args.get('auth').name))

            return args.get('auth')
        else:
            pass

    def _get_current_user(self, request):
        for item in self._get_tokens(request):
            if item.get('is_common'):
                return self._auth_middleware(item.get('token'))

    def check_login(func):
        async def _check(*args, **kwargs):
            user = args[0]._get_current_user(args[1])
            if user == None:
                raise aiohttp.web.HTTPFound('/login')

            return await func(*args)

        return _check

    def _getCustomRoutes(self):
        return [
            ('/login', self._login, ('get', 'post')),
            ('/logout', self._logout, ['get']),
        ]

    async def _login(self, request):
        if request.method == 'GET':
            return aiohttp_jinja2.render_template('login.html', request, {})
        else:
            try:
                response = aiohttp.web.HTTPFound('/')
                data = await request.post()
                token = await TokensGet().execute({
                    'username': data.get('username', '').strip(),
                    'password': data.get('password', '').strip(),
                    'infinite': True
                })
                _tokens = self._get_tokens(request)
                _tokens.append({
                    'token': token.items[0].value,
                    'is_common': True
                })

                response.set_cookie('tokens', JSON(data = _tokens).dump())

                return response
            except Exception as e:
                return aiohttp_jinja2.render_template('login.html', request, {'error': str(e)})

    async def _logout(self, request):
        response = aiohttp.web.HTTPFound('/')
        _tokens = self._get_tokens(request)
        for item in _tokens:
            item['is_common'] = False

        if request.rel_url.query.get('clear') == '1':
            _tokens = []

        response.set_cookie('tokens', JSON(data = _tokens).dump())

        return response

    @check_login
    async def _index(self, request):
        _context = self._get_template_context(request)
        file_name = 'index.html'
        query = request.rel_url.query
        _object_name = query.get('i')
        if _object_name != None:
            match (_object_name):
                case 'App.Objects.Index.ObjectsList':
                    file_name = 'namespaces.html'
                    _items = None

                    if query.get('name') != None:
                        _items = app.ObjectsList.get_namespace_with_name(query.get('name')).getItems()

                    _context.update({
                        'namespaces': app.ObjectsList.namespaces,
                        'objects': _items
                    })
                case 'App.Storage.Item.List':
                    file_name = 'storages.html'

                    _context.update({
                        'storages': app.Storage.items,
                    })
                case 'App.Storage.VirtualPath.Navigate':
                    file_name = 'virtual_path.html'
                    path = query.get('path')

                    _context.update({
                        'path': path,
                        'items': await Navigate().execute({
                            'path': path,
                            'count': 20,
                        }),
                    })
                case _:
                    _context.update({'error': 'Not found displayment for this'})

        return aiohttp_jinja2.render_template(file_name, request, _context)
