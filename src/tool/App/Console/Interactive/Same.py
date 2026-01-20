from App.Objects.Act import Act
from Data.Types.Int import Int
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Relations.Submodule import Submodule
from App.Console.Interactive.Interactive import Interactive
from App import app

class Same(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'index',
                orig = Int,
                default = -1,
            )
        ])

    @classmethod
    def _submodules(cls) -> list:
        return [
            Submodule(
                item = Interactive,
                role = ['allowed_view']
            )
        ]

    async def _implementation(self, i):
        old_i = app.app.view._history[i.get('index')]
        # TODO: add recursion protection

        return await app.app.view.pre_i.execute(old_i)
