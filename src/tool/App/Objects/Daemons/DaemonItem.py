from App.Objects.Object import Object
from App.Objects.Executable import Executable
from App.Storage.StorageUUID import StorageUUID
from pydantic import Field

class DaemonItem(Object):
    item: StorageUUID = Field(default = None)

    def get_item(self) -> Object:
        if self.item.isInstance(StorageUUID):
            return self.item.getItem()
        else:
            return self.item
