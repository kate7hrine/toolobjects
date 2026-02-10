from Data.Primitives.Collections.Collection import Collection
from App.Objects.Relations.Submodule import Submodule

class List(Collection):
    @classmethod
    def _submodules(cls) -> list:
        from Media.Images.List.Add import Add
        from Media.Images.Image import Image

        return [
            Submodule(
                item = Image,
                role = ['object']
            ),
            Submodule(
                item = Add,
                role = ['action']
            )
        ]
