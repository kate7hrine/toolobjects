from App.Objects.Object import Object
from App import app
from App.ACL.User import User
from App.ACL.GetHash import GetHash
from App.Objects.Custom.CustomNamespace import CustomNamespace

class PostRun(Object):
    @classmethod
    def mount(cls):
        # Appending settings
        for item in app.ObjectsList.getItems().toList():
            if item.is_inited == False:
                continue

            app.Config.appendModule(item.getModule())

        # loading custom
        _custom = CustomNamespace(
            name = 'custom'
        )
        for item in cls.getOption('objects.index.custom.objects'):
            _custom.append_by_id(item)

        app.ObjectsList.append_namespace(_custom)
        try:
            _custom.load()
        except Exception as e:
            _custom.log_error(e)

        app.ObjectsList.clear_cache()

        # Creating root user if he not exists
        default_root_password = 'root'
        has_root = False
        for user in app.AuthLayer.getUsers():
            if user.name == 'root':
                has_root = True

        if has_root == False:
            app.AuthLayer.add_user(User(
                    name = 'root',
                    # 2manywraps
                    password_hash = GetHash()._implementation({'string': default_root_password}).items[0].value
                )
            )
