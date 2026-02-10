from pydantic import Field, field_serializer
from App.Objects.Misc.CommonContainable import CommonContainable
from App.Objects.Relations.LinkInsertion import LinkInsertion
from App.DB.DBInsertable import DBInsertable
from typing import Any
from App import app

class Source(CommonContainable, DBInsertable):
    obj: LinkInsertion | Any = Field()

    # Very unoptimized>__<
    @field_serializer('obj')
    def get_obj(self, _obj) -> Any:
        try:
            if _obj.get('obj'):
                _val = app.ObjectsList.getByName(_obj.get('obj').get('saved_via').get('object_name'))

                return _val.getModule()(**_obj)
            
            if hasattr(_obj, '_link_insertion_type'):
                return self._get('obj')
        except Exception as e:
            return _obj
