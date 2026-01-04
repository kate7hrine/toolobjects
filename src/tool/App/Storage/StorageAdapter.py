from App.Objects.Protocol import Protocol
from typing import Any

class StorageAdapter(Protocol):
    _storage_item: Any = None
