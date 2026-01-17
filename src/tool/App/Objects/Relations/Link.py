from App.Objects.Mixins.Model import Model
from App.DB.DBInsertable import DBInsertable
from App.Objects.Relations.LinkInsertion import LinkInsertion
from App.Objects.Relations.LinkData import LinkData
from pydantic import Field, computed_field
from typing import Any

class Link(Model, DBInsertable):
    '''
    Link to an object.

    role is describes Link's relation to Object or its content

    object: related to internal content of Object
    thumbnail: related to Object's preview
    common: is common to object (storage unit or something)
    revision: another version of current object
    '''

    item: Any = Field()
    data: LinkData = Field(default = LinkData())

    def toInsert(self, field: list[str] = []) -> LinkInsertion:
        return LinkInsertion(
            link = self,
            field = field
        )
