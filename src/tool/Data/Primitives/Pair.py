from App.Objects.Object import Object
from pydantic import Field
from typing import Any

class Pair(Object):
    key: Any = Field(default = None)
    value: Any = Field(default = None)
