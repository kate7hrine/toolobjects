from App.Objects.Act import Act
from Media.Images.Image import Image
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Objects.Responses.ObjectsList import ObjectsList
from Data.Float import Float

class MakeImageThumbnail(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'image',
                orig = Image,
                assertions = [NotNoneAssertion()]
            ),
            Argument(
                name = 'percentage',
                orig = Float,
                default = 0.5
            )
        ])

    async def implementation(self, i):
        image = i.get('image')
        thumb = image._make_thumbnail(self._read_file(), i.get('percentage'))

        image.link(thumb.obj, role = ['thumbnail'])
        image._reset_file()

        return ObjectsList(items = [image])