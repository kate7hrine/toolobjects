from App.Objects.Object import Object
from pydantic import Field
from typing import Optional

class EntryContent(Object):
    type: Optional[str] = Field(default = 'html')
    content: str = Field()
