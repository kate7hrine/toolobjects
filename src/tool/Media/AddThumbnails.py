from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Assertions.NotNone import NotNone
from App.Objects.Responses.ObjectsList import ObjectsList
from App.Objects.Misc.Thumbnail import Thumbnail
from App.Objects.Act import Act
from Data.Types.String import String

class AddThumbnails(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'object',
                by_id = True,
                assertions = [NotNone()]
            ),
            ListArgument(
                name = 'items',
                orig = ObjectsList
            ),
            ListArgument(
                name = 'role',
                orig = String
            )
        ])

    async def _implementation(self, i):
        _object = i.get('object')
        _role = getattr(_object, 'thumbnail_type', [])
        if i.get('role') != None:
            _role = i.get('role')

        for item in i.get('items'):
            _object.local_obj.add_thumbnail(Thumbnail(
                obj = item,
                role = _role,
            ))
            _object.save()
