from App.Client.Displayment import Displayment
from App import app
import aiohttp_jinja2

class ObjectsList(Displayment):
    for_object = 'App.Objects.Index.ObjectsList'

    async def render_as_page(self, request, context):
        query = request.rel_url.query
        items = None

        if query.get('name') != None:
            items = app.ObjectsList.get_namespace_with_name(query.get('name')).getItems()

        context.update({
            'namespaces': app.ObjectsList.namespaces,
            'objects': items
        })

        return aiohttp_jinja2.render_template('namespaces.html', request, context)
