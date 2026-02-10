from App.Objects.Object import Object
from pydantic import Field
from typing import Optional
from datetime import datetime
from Web.Pages.Crawler.PageHTML import PageHTML
from App import app

class EntryContent(Object):
    type: Optional[str] = Field(default = 'html')
    content: str = Field(default = '')

    async def update(self):
        # TODO: download images
        pass
        #html = PageHTML.from_html(self.content)
        #tmp = app.Storage.get('tmp').storage_adapter.get_storage_unit()

        #self.link(tmp)

        #for item in html.get_media():
        #    item.download_function(tmp.getDir(), str(int(datetime.now())))

        #self.content = html.prettify()

    def get_html(self):

        html = PageHTML.from_html(self.content)
        html.clear_js()

        return html.prettify()
