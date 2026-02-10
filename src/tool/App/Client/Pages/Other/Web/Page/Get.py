from App.Client.Displayment import Displayment
from Web.Pages.Get import Get as PageGet
from App.Storage.Item.StorageItem import StorageItem
from App import app

class Get(Displayment):
    for_object = 'Web.Pages.Get'

    async def render_as_page(self, args = {}):
        orig_item = self.get_link_item()

        assert orig_item != None

        self.context.update({
            'item': orig_item,
            'args': args,
        })

        if self.is_post():
            data = await self.request.post()
            url = data.get('url')
            inline_css = data.get('inline_css')
            mode = 'Web.Pages.Crawler.Original'
            if inline_css == 'on':
                mode = 'Web.Pages.Crawler.Plain'

            assert url != '', 'url = null'

            _storage = None
            if orig_item.isInstance(StorageItem):
                _storage = orig_item
            else:
                _storage = app.Storage.get(orig_item.getDbName())

            items = await PageGet().execute({
                'url': url,
                'mode': mode
            })

            for item in items.getItems():
                item.local_obj.make_public()
                item.flush(_storage)

                if orig_item.isInstance(StorageItem) == False:
                    orig_item.link(item)

            return self.redirect('/?i=App.Objects.Object&uuids=' + items.get(0).getDbIds())

        return self.render_template('Other/Web/Page/get.html')
