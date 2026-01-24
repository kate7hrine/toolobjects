from App.Objects.Mixins.Model import Model
from pydantic import Field

class CommonContainable(Model):
    is_common: bool = Field(default = False)
