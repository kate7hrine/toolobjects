from App.Objects.Object import Object
from App.DB.ConnectionAdapter import ConnectionAdapter
from App.Storage.StorageAdapter import StorageAdapter
from pydantic import Field
from App import app

class StorageItem(Object):
    '''
    Implements storage with DB and storageunits.

    Notice: path is takes literally and does not creates additional dirs.
    path=f:/dir, name='dir' will use dir f:/dir.

    If 'path' not passed, it will use storage/dbs/{name} dir
    '''

    name: str = Field()

    # input
    storage_type: str = Field(default = 'double_divided_hash_dirs')
    storage: dict = Field(default = {})

    db_type: str = Field(default = None)
    db: dict = Field(default = {})
    # /input

    root_uuid: int = Field(default = None)
    allowed_objects: list[str] = Field(default = None)
    forbidden_objects: list[str] = Field(default = None)

    # display_name: str = Field(default = None)

    # Internal usage only
    adapter: ConnectionAdapter = Field(default = None, exclude = True)
    storage_adapter: StorageAdapter = Field(default = None, exclude = True)

    def get_db_adapter(self) -> ConnectionAdapter:
        assert self.has_db_adapter(), "storage item {0} does not has db connection".format(self.name)

        return self.adapter

    def get_storage_adapter(self) -> StorageAdapter:
        assert self.has_storage_adapter(), "storage item {0} does not has storage".format(self.name)

        return self.storage_adapter

    def has_db_adapter(self) -> bool:
        return self.adapter != None

    def has_storage_adapter(self) -> bool:
        return self.storage_adapter != None

    def _init_hook(self):
        if self.db_type != None:
            self.adapter = self._get_adapter_by_name(self.db_type, self.db)

        if self.storage_type != None:
            self.storage_adapter = self._get_adapter_by_name(self.storage_type, self.storage, ['App', 'Storage', 'Adapters'])

    def _get_adapter_by_name(self, adapter_name: str, unwrap_dict: dict = {}, group: list[str] = ['App', 'DB', 'Adapters']):
        for adapter in app.ObjectsList.getByName(group):
            _module = adapter.getModule()
            if _module.protocol_name == adapter_name:
                item = _module(**unwrap_dict)
                item._storage_item = self
                item._init_hook()

                return item

    @classmethod
    def asArgument(cls, val: str):
        if type(val) == str:
            return app.Storage.get(val)

        return super().asArgument(val)
