from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Object import Object
from App.Objects.Responses.ObjectsList import ObjectsList
from Data.Types.String import String
from Data.Types.Boolean import Boolean

class Local(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            ListArgument(
                name = 'object',
                by_id = True,
                orig = Object
            ),
            Argument(
                name = 'name',
                orig = String
            ),
            Argument(
                name = 'description',
                orig = String
            ),
            Argument(
                name = 'collection',
                orig = Boolean
            ),
            Argument(
                name = 'public',
                orig = Boolean
            )
        ])

    async def _implementation(self, i):
        items = ObjectsList(items = [], unsaveable = True)
        for obj in i.get('object'):
            for key in i.compare.toNames():
                if key in ['object']:
                    continue

                new = i.get(key)
                if new == None:
                    continue

                setattr(obj.local_obj, key, new)

            obj.local_obj.set_edited()
            obj.save()

            items.append(obj)

        return items
