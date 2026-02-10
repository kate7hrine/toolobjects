from App.Client.Displayment import Displayment
from App import app

class Create(Displayment):
    for_object = 'App.Objects.Operations.Create'

    async def render_as_page(self, args = {}):
        query = self.request.rel_url.query
        creates = app.ObjectsList.get_creations()
        self.context.update({
            'creations': creates,
            'ref': query.get('ref'),
            'storage': query.get('storage'),
            'db_item': query.get('db_item'),
        })

        return self.render_template('Actions/create.html')
