from App.Objects.Object import Object
from pydantic import Field

class Text(Object):
    text: str = Field(default = '')
