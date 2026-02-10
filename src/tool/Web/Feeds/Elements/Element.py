from App.Objects.Object import Object
from pydantic import Field
from typing import Optional
from Web.Feeds.Elements.Link import Link
import xml.etree.ElementTree as ET

class Element(Object):
    id: Optional[str] = Field(default = None)
    title: Optional[str] = Field(default = None)
    subtitle: Optional[str] = Field(default = None)
    description: Optional[str] = Field(default = None)
    link_item: Optional[Link] = Field(default = None)

    def from_xml(self, data: ET):
        pass
