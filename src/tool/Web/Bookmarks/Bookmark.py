from App.Objects.Object import Object
from App.Storage.StorageUnitLink import StorageUnitLink
from pydantic import Field

class Bookmark(Object):
    url: str = Field(default = None)
    open_in_new_page: bool = Field(default = True)
    favicon: StorageUnitLink = Field(default = None)

    def get_favicon_url(self):
        return self._get('favicon').get_storage_unit().get_url() + 'favicon.ico'
