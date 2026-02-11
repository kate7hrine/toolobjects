from App.Client.Displayment import Displayment
from App import app

class Create(Displayment):
    for_object = 'App.Objects.Operations.Create'

    async def render_as_page(self, args = {}):
        query = self.request.rel_url.query
        item = self.get_link_item()

        assert item != None

        creates = app.ObjectsList.get_creations()
        object_creations = item.get_creations()
        if len(object_creations) > 0:
            creates = object_creations

        self.context.update({
            'creations': creates,
            'ref': query.get('ref'),
            'storage': query.get('storage'),
            'db_item': query.get('db_item'),
        })

        return self.render_template('Actions/create.html')
