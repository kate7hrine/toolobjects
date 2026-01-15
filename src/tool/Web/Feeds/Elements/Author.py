from App.Objects.Object import Object
from pydantic import Field

class Author(Object):
    name: str = Field()
    email: str = Field()
