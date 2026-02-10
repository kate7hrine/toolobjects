from App.Objects.Mixins.BaseModel import BaseModel
from App.DB.DBInsertable import DBInsertable
from pydantic import Field, computed_field
from typing import Literal
from enum import Enum

class LinkData(BaseModel, DBInsertable):
    role: list[Literal['object', 'thumbnail', 'common', 'revision', 'list_item'] | str] = Field(default = ['object'])

    @computed_field
    @property
    def is_common(self) -> bool:
        return 'common' in self.data.role

    @computed_field
    @property
    def is_internal(self) -> bool:
        return 'external' not in self.data.role

    @computed_field
    @property
    def is_external(self) -> bool:
        return 'external' in self.data.role
