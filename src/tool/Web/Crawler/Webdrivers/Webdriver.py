from App.Objects.Object import Object
from App.Objects.Relations.LinkInsertion import LinkInsertion
from typing import ClassVar
from pydantic import Field

class Webdriver(Object):
    webdriver_name: ClassVar[str] = 'none'
    platform: str = Field(default = None)
    file: LinkInsertion = Field(default = None)
