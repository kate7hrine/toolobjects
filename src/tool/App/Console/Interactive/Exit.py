from App.Objects.Act import Act
from App.Console.Interactive.Interactive import Interactive
from App.Objects.Relations.Submodule import Submodule

class Exit(Act):
    @classmethod
    def _submodules(cls) -> list:
        return [
            Submodule(
                item = Interactive,
                role = ['allowed_view']
            )
        ]

    def _implementation(self, i):
        raise KeyboardInterrupt('exit')
