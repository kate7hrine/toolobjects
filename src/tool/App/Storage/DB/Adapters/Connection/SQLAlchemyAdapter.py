from App.Storage.DB.Adapters.ConnectionAdapter import ConnectionAdapter
from App.Storage.DB.Adapters.ObjectAdapter import ObjectAdapter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, event, String
from snowflake import SnowflakeGenerator
from typing import Any
import json

class SQLAlchemyAdapter(ConnectionAdapter):
    _engine: Any = None
    _session: Any = None
    ObjectUnit: Any = None
    ObjectUnitLink: Any = None

    def _init_models(self):
        Base = declarative_base()
        _id_gen = SnowflakeGenerator(32)

        class ObjectUnit(ObjectAdapter, Base):
            __tablename__ = 'objects'
            uuid = Column(Integer(), primary_key=True)
            content = Column(String(), nullable=False)

        class ObjectUnitLink(ObjectAdapter, Base):
            __tablename__ = 'links'
            uuid = Column(Integer(), primary_key=True)

        @event.listens_for(ObjectUnit, 'before_insert', propagate=True)
        @event.listens_for(ObjectUnitLink, 'before_insert', propagate=True)
        def receive_before_insert(mapper, connection, target):
            if target.uuid is None:
                target.uuid = next(_id_gen)

        self.ObjectUnit = ObjectUnit
        self.ObjectUnitLink = ObjectUnitLink

        Base.metadata.create_all(self._engine)

    def _get_engine(self, connection_str: str):
        pass

    def insertObject(self, obj: Any):
        from sqlalchemy.orm import Session

        unit = None

        with self._session as session:
            unit = self.ObjectUnit(
                content=json.dumps(
                    obj.to_json()
                )
            )
            session.add(unit)
            session.commit()

            return unit

    def search(self):
        pass
