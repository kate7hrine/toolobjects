from App.Objects.Object import Object
from Web.Feeds.Elements.Element import Element
from pydantic import Field
from typing import Optional
from datetime import datetime
import xml.etree.ElementTree as ET

class Channel(Element):
    url: str | None = Field(default = None)
    channel_link: str = Field(default = None)
    generator: str | None = Field(default = None)
    copyright: str | None = Field(default = None)
    language: str | None = Field(default = None)
    ttl: int | None = Field(default = None)

    def get_original_url(self):
        return self.obj.source[0].obj.get('value')
