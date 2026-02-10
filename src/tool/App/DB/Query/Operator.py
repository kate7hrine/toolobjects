from App.Objects.Mixins.BaseModel import BaseModel
from typing import ClassVar

class Operator(BaseModel):
    operator: ClassVar[str] = ''

    def _implementation(self, condition):
        pass
