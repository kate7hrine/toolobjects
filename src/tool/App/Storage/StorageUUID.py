from App.Objects.Object import Object
from typing import Self
from pydantic import Field
from App import app

class StorageUUID(Object):
    '''
    Object by id and storage name
    '''

    storage: str = Field()
    uuid: int = Field()

    @classmethod
    def asArgument(cls, val: str | dict):
        if isinstance(val, StorageUUID):
            return val

        _storage = None
        if type(val) == str:
            vals = val.split('_', 1)

            _storage = StorageUUID(storage = vals[0], uuid = vals[1])
        if type(val) == dict:
            _storage = StorageUUID(storage = val.get('storage'), uuid = val.get('uuid'))

        return _storage

    @staticmethod
    def validate(string: str) -> bool:
        if isinstance(string, str) == False:
            return False

        return len(string.split('_')) == 2

    @classmethod
    def fromString(cls, string: str) -> Self:
        _ids = string.split('_', 1)
        return cls(
            storage = _ids[0],
            uuid = _ids[1]
        )

    def getId(self):
        return f"{self.storage}_{self.uuid}"

    def getStorage(self):
        return app.Storage.get(self.storage)

    def getItem(self):
        if self.uuid == None:
            return None

        _storage = self.getStorage()

        assert _storage != None, "storage with name {0} not found".format(self.storage)

        return _storage.adapter.ObjectAdapter.getById(self.uuid)

    def toPython(self):
        _item = self.getItem()
        if _item == None:
            return None

        return _item.toPython()
