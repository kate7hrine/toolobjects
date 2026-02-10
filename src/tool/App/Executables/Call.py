from App.Objects.Object import Object
from pydantic import Field
from App import app

class Call(Object):
    id: int = Field(default = 0)
    predicate: str = Field(default = None)
    arguments: dict = Field(default = {})

    def constructor(self):
        self.id = app.app.executables_id.getIndex()
