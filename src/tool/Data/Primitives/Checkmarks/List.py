from Data.Primitives.Checkmarks.Checkmark import Checkmark
from App.Objects.Act import Act
from typing import Generator
from App.Objects.Relations.Submodule import Submodule
from Data.Primitives.Collections.Collection import Collection

class List(Collection):
    @classmethod
    def _submodules(cls):
        return [
            Submodule(
                item = Checkmark,
                role = ['link_allowed']
            )
        ]

    def getCheckmarks(self) -> Generator[Checkmark]:
        for link in self.getLinked():
            item = link.item
            if item.isInstance(Checkmark):
                yield item

    def _display_as_string(self):
        _out = f"Checkmarks list \"{str(self.obj.name)}\""
        _out += "\n"

        for checkmark in self.getCheckmarks():
            _out += checkmark.displayAsString()

        _out += "\n"

        return _out
