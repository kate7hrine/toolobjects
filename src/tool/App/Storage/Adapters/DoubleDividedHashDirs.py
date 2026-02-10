from App.Storage.StorageAdapter import StorageAdapter
from pydantic import Field
from pathlib import Path
from App.Storage.StorageUnit import StorageUnit
from App import app
import secrets

class DoubleDividedHashDirs(StorageAdapter):
    protocol_name = 'double_divided_hash_dirs'
    storage_dir_name: str = Field(default = 'storage')
    directory: str = Field(default = None)
    _path: str = None

    def _init_hook(self):
        if self.directory != None:
            self._path = Path(self.directory)
            if self._path.is_file() == True:
                self.log_error(f"storage item {self._storage_item.name}: path is file")
            if self._path.exists() == False:
                self._path.mkdir()
        else:
            dbs_dir = app.app.storage.joinpath('dbs')
            self._path = dbs_dir.joinpath(self._storage_item.name)
            self._path.mkdir(exist_ok=True)

        self.getStorageDir().mkdir(exist_ok=True)

    def getStorageUnit(self) -> StorageUnit:
        _bytes = 32
        _hash = secrets.token_hex(_bytes)
        _item = StorageUnit()
        _item.fromDir(self.getStorageDir(), _hash)
        _item._init_hook()

        return _item

    def getStorageDir(self):
        return self._path.joinpath(self.storage_dir_name)

    def getDir(self):
        return self._path
