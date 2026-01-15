from Web.Feeds.Elements.Element import Element
from Web.Feeds.Elements.EntryContent import EntryContent
from pydantic import Field
from typing import Optional
import datetime

class Entry(Element):
    summary: str = Field(default = None)
    content: EntryContent = Field(default = None)

    def set_pubdate(self, date: datetime.datetime):
        self.obj.created_at = date
