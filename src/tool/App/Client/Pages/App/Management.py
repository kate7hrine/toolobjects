from App.Client.Displayment import Displayment
import aiohttp_jinja2

class Management(Displayment):
    for_object = 'App'

    async def render_as_page(self, request, context):
        return aiohttp_jinja2.render_template('management.html', request, context)
