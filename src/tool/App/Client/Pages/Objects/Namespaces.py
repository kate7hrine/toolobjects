from App.Client.Displayment import Displayment
from App.Client.Menu.Item import Item
from App import app
import aiohttp_jinja2

class Namespaces(Displayment):
    for_object = 'App.Objects.Index.GetList'

    async def render_as_page(self, args = {}):
        enabled = list()
        other = list()

        for namespace in app.ObjectsList.namespaces:
            if namespace.name in app.ObjectsList.current:
                enabled.append(namespace)
            else:
                other.append(namespace)

        self.context.update({
            'enabled': enabled,
            'other': other,
            'namespaces': app.ObjectsList.namespaces,
            'enabled_namespaces': app.ObjectsList.current,
        })

        return self.render_template('Objects/namespaces.html')
