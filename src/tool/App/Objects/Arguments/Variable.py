from App.Objects.Arguments.Argument import Argument
from pydantic import Field
from typing import Any

class Variable(Argument):
    value: Any = Field(default = None)

    def init_hook(self):
        pass
