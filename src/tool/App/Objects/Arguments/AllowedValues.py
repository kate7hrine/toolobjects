from App.Objects.Object import Object
from pydantic import Field

class AllowedValues(Object):
    values: list = Field(default = [])
    strict: bool = Field(default = True)
