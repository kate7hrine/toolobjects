from App.Objects.Object import Object
from Web.Pages.Crawler.PageHTML import PageHTML
from Web.Pages.Crawler.Webdrivers.GotRequest import GotRequest
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ListArgument import ListArgument

from Data.Types.Boolean import Boolean
from Data.Types.String import String

from Web.Pages.Page import Page
from Web.Pages.Assets.Asset import Asset
from typing import Any
from urllib.parse import urlparse
from pydantic import Field
import urllib
import asyncio

class Original(Object):
    url_override: str = Field(default = None)
    ref: Any = Field(default = None)

    async def register(self, page):
        self.log('registing page')

        async def _request(request):
            page._page.got_assets.append(GotRequest(
                url = request.url,
                request = request,
                done = False
            ))

        async def _response(response):
            request = None
            for item in page._page.got_assets:
                if item.url == response.url:
                    request = item

            if request == None:
                return

            #self.log('request {0}, method {1}'.format(response.url, request.request.method))

            if request.request.method == 'GET':
                request.asset = Asset(url=response.url)
                _dir = page.html.get_assets_dir()
                _dir = _dir.joinpath(request.asset.get_encoded_url())

                with open(str(_dir), 'wb') as _file:
                    _file.write(await response.body())

                self.log('downloaded {0}'.format(response.url))

            request.done = True

        page._page._page.on('request', _request)
        page._page._page.on('response', _response)

    async def crawl(self, page: Page, i: dict):
        await page.set_info()

        if i.get('scroll_down'):
            await page._page.scroll_down(i.get('web.crawler.scroll_down.cycles'), i.get('web.crawler.scroll_down.'))

        page.html.encoding = await page.get_encoding()

        await asyncio.sleep(2)

        html = PageHTML.from_html(await page._page.get_html())
        if page.html.encoding == None:
            page.html.encoding = html.encoding

        #if i.get('download.favicon') == True:
        #self.log('setting favicons...')

        results = dict()
        for key in ['get_favicons', 'get_images', 'get_links', 'get_scripts']:
            if results.get(key) == None:
                results[key] = list()

            self.log('getting {0}...'.format(key[4:]))

            for item in getattr(html, key)(page):
                found_asset = None
                for asset in page._page.got_assets:
                    if asset.url_matches(item.url):
                        found_asset = asset

                if found_asset == None and item.has_url():
                    try:
                        await item.download_function(page.html.get_assets_dir())
                    except Exception as e:
                        self.log_error(e, exception_prefix='assets downloading error: ')

                item.replace()
                results[key].append(item)

        for item in results.get('get_favicons'):
            page.favicons.append(item)

        for meta in html.get_meta(page):
            _name = meta.get_name()
            if _name == None:
                self.log('metatag {0} = {1}'.format(_name, meta.get_content()))
            else:
                self.log('metatag: no name')

            page.meta_tags.append(meta)

        page.html.write(html.prettify())

    @classmethod
    def getArguments(cls):
        return ArgumentDict(items = [
            Argument(
                name = 'download.favicon',
                orig = Boolean,
                default = True
            ),
            Argument(
                name = 'data.meta',
                orig = Boolean,
                default = True
            ),
            Argument(
                name = 'download.media',
                orig = Boolean,
                default = True
            ),
            ListArgument(
                name = 'download.media.selectors',
                orig = String,
                default = True
            ),
            Argument(
                name = 'data.save_urls',
                orig = Boolean,
                default = True
            ),
        ])
