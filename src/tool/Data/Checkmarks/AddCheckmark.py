from App.Objects.Act import Act
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Responses.ObjectsList import ObjectsList
from Data.Checkmarks.Checkmark import Checkmark
from Data.Checkmarks.List import List
from Data.String import String

class AddCheckmark(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'list',
                id_allow = True,
                orig = List
            ),
            Argument(
                name = 'label',
                default = False,
                literally = True,
                orig = String
            )
        ])

    def implementation(self, i):
        _label = i.get('label')
        checkmarks = i.get('list')

        checkmark = Checkmark()
        checkmarks.link(checkmark)
        checkmark.label = checkmark.link(_label).toInsert()
        checkmark.save()

        return ObjectsList(items = [checkmarks])
