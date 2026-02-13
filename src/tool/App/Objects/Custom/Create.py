from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Responses.ObjectsList import ObjectsList
from App.Objects.Arguments.Assertions.NotNone import NotNone
from App.Objects.Custom.CustomObject import CustomObject
from Data.Types.String import String
from Data.Types.Boolean import Boolean

class Create(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'name',
                orig = String,
                assertions = [NotNone()]
            ),
            ListArgument(
                name = 'extends_from',
                orig = String,
            ),
            Argument(
                name = 'save_to_config',
                orig = Boolean,
                default = True
            )
        ])

    async def _implementation(self, i):
        extends_from = i.get('extends_from')
        returns = ObjectsList(items = [])
        c = CustomObject(
            name = i.get('name'),
        )

        if len(extends_from) > 0:
            c.extends_from = extends_from

        returns.append(c)

        return returns
