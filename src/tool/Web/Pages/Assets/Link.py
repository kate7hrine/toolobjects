from Web.Pages.Assets.Asset import Asset
from pydantic import Field

class Link(Asset):
    rel: list[str] = Field(default = [])
    media: str = Field(default = None)
    type: str = Field(default = None)
    as_item: str = Field(default = None, alias = 'as')

    def should_download(self):
        if 'alternate' in self.rel:
            # self.log('assets: links: {0} is alternate, so dont downloading it'.format(item))
            return False

        if self.type == None and self.as_item == None and self.rel == None:
            return False

        return True
