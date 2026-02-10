from App.Objects.Object import Object
from pydantic import Field

class Item(Object):
    args: dict = Field(default = {})
    unused: bool = Field(default = False)
