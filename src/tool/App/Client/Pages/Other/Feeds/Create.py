from App.Client.Displayment import Displayment
from Web.Feeds.Create import Create as FeedCreate
from App.Storage.Item.StorageItem import StorageItem

class Create(Displayment):
    for_object = 'Web.Feeds.Create'

    async def render_as_page(self, args = {}):
        query = self.request.rel_url.query
        item = self.get_link_item()

        assert item != None

        self.context.update({
            'item': item,
            'args': args,
        })

        if self.is_post():
            data = await self.request.post()
            url = data.get('url')

            assert url != '', 'url = null'

            refresh_every = data.get('refresh_every', None)

            _storage = None
            if item.isInstance(StorageItem):
                _storage = item.name
            else:
                _storage = item.getDbName()

            items = await FeedCreate().execute({
                'url': url,
                'refresh_every': refresh_every,
                'save_to': [_storage]
            })

            for item in items.getItems():
                item.local_obj.make_public()

            return self.redirect('/?i=App.Objects.Object&uuids=' + items.get(0).getDbIds())

        return self.render_template('Other/Feeds/create.html')
