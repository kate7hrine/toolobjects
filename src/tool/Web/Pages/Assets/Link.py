from Web.Pages.Assets.Asset import Asset
from pydantic import Field

class Link(Asset):
    rel: str = Field(default = None)
