from App.Objects.Thumbnail import Thumbnail
from Media.Images.Image import Image
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Responses.ObjectsList import ObjectsList
from Data.Types.Float import Float
from pathlib import Path

class ResizeByPercentage(Thumbnail):
    thumb_for = Image

    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'percentage',
                orig = Float,
                default = 0.5
            )
        ])

    async def _implementation(self, i):
        image = i.get('object')
        percentage = i.get('percentage')

        _img = image._read_file()

        sizes = (_img.size[0], _img.size[1])
        new_sizes = (int(sizes[0] * percentage), int(sizes[1] * percentage))
        resized_img = _img.resize(new_sizes)
        resized_img.convert('RGB')

        thumb_image = Image()
        thumb_image.move(image)
        thumb_image._set_dimensions(resized_img)

        filename = Path(_img.filename)
        new_file_name = filename.stem + '_thumb_' + str(percentage) + filename.suffix
        new_name = filename.with_name(new_file_name)
        resized_img.save(new_name)

        thumb_image.set_insertion_name(new_file_name)

        image._reset_file()

        return ObjectsList(items = [thumb_image])
