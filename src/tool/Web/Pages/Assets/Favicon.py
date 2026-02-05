from Web.Pages.Assets.Asset import Asset
from App.Objects.Object import Object
from pydantic import Field
from typing import Optional

class Favicon(Object, Asset):
    sizes: Optional[str] = Field(default = None)
