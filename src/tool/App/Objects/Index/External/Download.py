from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from Data.Boolean import Boolean
from Data.String import String
from App import app

class Download(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'url',
                orig = String,
            ),
            Argument(
                name = 'path',
                orig = String,
            ),
            Argument(
                name = 'confirm',
                orig = Boolean,
                default = False
            )
        ])

    async def _implementation(self, i):
        if i.get('confirm') == False:
            self.log('The installed plugins will have full access to your system. If you trust this URL, set the \'confirm\' = True')

            return

        _namespaces = app.app.src.joinpath('namespaces')
