from App.Objects.Mixins.BaseModel import BaseModel
from typing import Any
from pydantic import Field

class Condition(BaseModel):
    val1: Any = Field()
    operator: str | Any = Field(default = None)
    val2: Any = Field(default = None)
    json_fields: list = Field(default = None)

    def getFirst(self):
        return self.val1

    def getLast(self):
        return self.val2
