from App.Objects.Misc.Valueable import Valueable
from App.Objects.Act import Act
from typing import Optional
from pydantic import Field

# It should be named as "Integer" btw
class Int(Valueable):
    value: int = None
    min_value: Optional[int | float] = Field(default = None)
    max_value: Optional[int | float] = Field(default = None)

    def _display_as_string(self):
        return str(self.value)

    @classmethod
    def asArgument(cls, val):
        if val == None:
            return None

        return int(val)

    def asArgumentAsInstance(self, val):
        if val == None:
            return None

        _val = self.asArgument(val)
        if self.min_value != None:
            assert _val > self.min_value, 'number is too short'

        if self.max_value != None:
            assert _val < self.max_value, 'number is too big'

        return _val
