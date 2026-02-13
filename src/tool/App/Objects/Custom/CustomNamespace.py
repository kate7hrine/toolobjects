from App.Objects.Index.Namespaces.Namespace import Namespace
from App.Objects.Index.LoadedObject import LoadedObject
from App.Objects.Custom.CustomLoadedObject import CustomLoadedObject
from typing import Generator
from pydantic import Field

class CustomNamespace(Namespace):
    ids: list = Field(default = [])

    def append_by_id(self, item):
        self.ids.append(item)

    def scan(self) -> Generator[LoadedObject]:
        for id in self.ids:
            yield CustomLoadedObject(id = id)
