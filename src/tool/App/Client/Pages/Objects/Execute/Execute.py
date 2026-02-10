from App.Client.Displayment import Displayment
from App.Objects.Operations.DefaultExecutorWheel import DefaultExecutorWheel
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from Data.Types.JSON import JSON
from App import app
import aiohttp_jinja2

class Execute(Displayment):
    for_object = 'App.Objects.Operations.DefaultExecutorWheel'

    async def render_as_page(self, request, context):
        query = request.rel_url.query
        name = query.get('name')

        _obj = app.ObjectsList.getByName(name)

        assert _obj != None, 'not found object'
        assert _obj.is_inited, 'not inited'

        obj = _obj.getModule()

        if request.method == 'POST':
            _params = dict(await request.post())
            _vals = {
                'i': obj._getNameJoined(),
                'auth': self.auth
            }
            for key, val in _params.items():
                if val == None or val == '':
                    continue

                _vals[key] = val

            stay = _params.get('stay') == '1'

            results = await DefaultExecutorWheel().execute(i = _vals)
            json = results.to_json()

            if stay == False:
                return self.return_json(json)
            else:
                context.update({
                    'obj': obj,
                    'data': JSON(data = json).dump(4)
                }) 

        context.update({
            'obj': obj
        })

        context['arguments'] = ArgumentDict()
        if hasattr(obj, 'getArguments'):
            context.update({
                'arguments': obj.getArguments(include_usage = True)
            })

        _args = DefaultExecutorWheel.getArguments()
        context['arguments'].join(_args, except_those = ['i'])

        return aiohttp_jinja2.render_template('Objects/Execute/nonjs_execute.html', request, context)
