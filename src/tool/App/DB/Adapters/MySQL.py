from App.DB.Adapters.SQLAlchemy import SQLAlchemy
from App.DB.Query.Condition import Condition
from pydantic import Field

class MySQL(SQLAlchemy):
    # Not tested

    protocol_name = 'mysql+pymysql'
    username: str = Field()
    password: str = Field(default = None)
    host: str = Field()
    port: int = Field()
    db_name: str = Field(default = None)
    charset: str = Field(default = 'utf8mb4')

    def _before_init_models(self):
        from sqlalchemy_utils import database_exists, create_database

        if not database_exists(self._engine.url): 
            create_database(self._engine.url)
