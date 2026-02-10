from App.Client.Displayment import Displayment
import aiohttp

class Page(Displayment):
    for_object = 'Web.Pages.Page'

    async def render_as_object(self, item):
        _html = ''

        print(item._get('html').get_main())
        self.context.update({
            'item': item,
            'html': _html
        })

        return self.render_string('Other/Web/page.html')
