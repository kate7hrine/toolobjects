from App.Objects.Object import Object
from pydantic import Field
from typing import Any
from Web.Pages.Assets.Asset import Asset

class GotRequest(Object):
    url: str = Field(default = None)
    response: Any = Field(default = None)
    asset: Asset = Field(default = None)
    done: bool = Field(default = False)

    def url_matches(self, url: str):
        _s = self.url.replace('https://', '').replace('http://', '')
        _f = url.replace('https://', '').replace('http://', '')
        return _s == _f
