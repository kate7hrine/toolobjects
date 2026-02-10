from App.Objects.Object import Object
from pydantic import Field

class LogPrefix(Object):
    name: str = Field(default="")
    id: int = Field(default=0)

    def toString(self):
        return f"{self.name}->{self.id}"
