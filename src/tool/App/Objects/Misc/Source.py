from App.Objects.Mixins.Model import Model
from pydantic import Field
from typing import Any

class Source(Model):
    obj: Any = Field()
    is_common: bool = Field(default = False)
