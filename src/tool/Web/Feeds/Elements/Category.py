from App.Objects.Object import Object
from pydantic import Field

class Category(Object):
    term: str = Field(default = None)
    label: str = Field(default = None)
