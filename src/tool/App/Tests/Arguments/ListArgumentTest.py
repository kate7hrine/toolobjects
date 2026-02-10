from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from Data.Types.List import List
from Data.Types.String import String

class ListArgumentTest(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'lists',
                orig = List(
                    value = [
                        String
                    ]
                ),
                config_fallback = ('app.name', False)
            )
        ])

    async def _implementation(self, i):
        self.log_raw(i.get('lists'))
