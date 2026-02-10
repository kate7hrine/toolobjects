from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Responses.ObjectsList import ObjectsList
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.String import String

class Items(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'items',
                orig = ObjectsList,
                assertions = [NotNoneAssertion()]
            ),
            Argument(
                name = 'directory',
                orig = String,
                assertions = [NotNoneAssertion()]
            )
        ])

    async def implementation(self, i):
        _items = i.get('items')
        _directory = i.get('directory')

        for item in _items:
            pass
