from App.Client.Displayment import Displayment
from App.Client.Menu.Item import Item
from App import app

class Storages(Displayment):
    for_object = 'App.Storage.Item.List'

    async def render_as_page(self, args = {}):
        query = self.request.rel_url.query
        show_internal = query.get('show_internal') == 'on'

        self.context.update({
            'storages': app.Storage.getAll(show_internal),
            'show_internal': show_internal
        })

        return self.render_template('Storage/storages.html')
