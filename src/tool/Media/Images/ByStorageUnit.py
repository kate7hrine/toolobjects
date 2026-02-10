from App.Objects.Extractor import Extractor
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Assertions.NotNone import NotNone
from App.Objects.Arguments.Argument import Argument
from App.Storage.StorageUnit import StorageUnit
from Media.Images.Image import Image

class ByStorageUnit(Extractor):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'storage_unit',
                by_id = True,
                orig = StorageUnit,
                assertions = [NotNone()]
            )
        ])

    async def _implementation(self, i):
        image = Image()
        image.set_storage_unit(i.get('storage_unit'))

        self.append(image)
