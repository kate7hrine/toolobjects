from App.Client.Displayment import Displayment
from App import app
import aiohttp_jinja2

class ObjectsList(Displayment):
    for_object = 'App.Objects.Index.ObjectsList'

    async def render_as_page(self, request, context):
        namespace = app.ObjectsList.get_namespace_with_name()
        objects = namespace.getItems()

        context.update({
            'namespace': namespace,
            'objects': objects
        })

        return aiohttp_jinja2.render_template('Objects/objects_list.html', request, context)
