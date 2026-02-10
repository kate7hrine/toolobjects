from App.Client.Displayment import Displayment
from Web.Pages.Crawler.PageHTML import PageHTML
import aiohttp

class Page(Displayment):
    for_object = 'Web.Pages.Page'
    prefer_object_displayment = 'page'

    async def render_as_page(self):
        item = self.context.get('item')
        hide_banner = self.request.query.get('hide_banner') == '1'
        html_path = item._get('html').get_main()
        html = html_path.read_text(encoding = item.html.encoding)

        html = PageHTML.from_html(html)
        html.make_correct_links(item)
        head_html = html.move_head()

        self.context.update({
            'item': item,
            'head_html': head_html,
            'html': html.prettify(),
            'hide_banner': hide_banner
        })

        return self.render_template('Other/Web/page.html')
