from App.Client.Displayment import Displayment
from App.Storage.Clear import Clear as RealClear
from App.Storage.ClearTemp import ClearTemp

class Clear(Displayment):
    for_object = 'App.Storage.Clear'

    async def render_as_page(self, args = {}):
        query = self.request.rel_url.query
        storage_name = query.get('name')
        self.context.update({
            'ref': query.get('ref')
        })

        if self.is_post():
            data = await self.request.post()
            act = data.get('act')

            match (act):
                case 'storage':
                    await RealClear().execute({
                        'storage': storage_name
                    })
                case 'tmp':
                    await ClearTemp().execute({
                        'storage': storage_name
                    })

            return self.redirect('/?i=App.Storage.Item.Get&name=' + storage_name)

        return self.render_template('Storage/clear.html')
