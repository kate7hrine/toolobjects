from App.Objects.Mixins.Model import Model
from pydantic import Field

class Source(Model):
    obj: Model = Field()
    is_common: bool = Field(default = False)
