from App.Objects.Misc.CommonContainable import CommonContainable
from pydantic import Field

class Geo(CommonContainable):
    lat: float = Field(default = None)
    long: float = Field(default = None)
