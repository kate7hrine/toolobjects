from App.DB.Adapters.SQLAlchemy import SQLAlchemy

class PostgreSQL(SQLAlchemy):
    # not implemented
    protocol_name = 'postgresql+pg8000'
