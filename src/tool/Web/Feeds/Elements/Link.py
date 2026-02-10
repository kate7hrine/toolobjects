from App.Objects.Object import Object
from typing import Literal, Optional
from pydantic import Field

class Link(Object):
    value: Optional[str] = Field(default = None)
    rel: Optional[str | Literal['alternate', 'related', 'self', 'enclosure', 'via']] = Field(default = None)
    type: Optional[str] = Field(default = None)
    hreflang: Optional[str] = Field(default = None)
    title: Optional[str] = Field(default = None)
    length: Optional[str] = Field(default = None)
