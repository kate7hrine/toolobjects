from App.Objects.Mixins.Model import Model
from pydantic import Field
from typing import Literal, Optional

class Thumbnail(Model):
    role: Optional[list[Literal['image', 'video']]] = Field(default = [])
    obj: Model = Field()
