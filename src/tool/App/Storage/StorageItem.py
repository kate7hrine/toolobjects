from App.Objects.Object import Object
from pydantic import Field

class StorageItem(Object):
    name: str = Field()
    display_name: str = Field(default = None)
