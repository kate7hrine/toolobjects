from App.DB.Adapters.SQLAlchemy import SQLAlchemy
from App.DB.Query.Condition import Condition
from pydantic import Field

class SQLite(SQLAlchemy):
    protocol_name = 'sqlite'
    content: str = Field(default = None)
    delimiter = ':///'

    def _get_sqlalchemy_connection_string(self):
        if self.content != None:
            return str(self.content)
        else:
            return str(self._storage_item.get_storage_adapter().getDir().joinpath(self.name + '.db'))
