from App.Storage.StorageUnit import StorageUnit
from App.Objects.Protocol import Protocol
from App.Objects.Object import Object
from typing import Any
from abc import abstractmethod

class StorageAdapter(Object, Protocol):
    _storage_item: Any = None

    @abstractmethod
    def get_storage_unit(self) -> StorageUnit:
        ...

    @abstractmethod
    def copy_storage_unit(self, unit: StorageUnit, change_common: bool = True):
        ...

    @abstractmethod
    def clear(self, unit: StorageUnit, change_common: bool = True):
        ...
