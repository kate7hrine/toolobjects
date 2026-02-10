from App.Objects.Object import Object
from pydantic import Field

class Geo(Object):
    lat: float = Field(default = None)
    long: float = Field(default = None)
