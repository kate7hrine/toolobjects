from pydantic import Field, field_serializer
from App.Objects.Misc.CommonContainable import CommonContainable
from typing import Any
from App import app

class Source(CommonContainable):
    obj: Any = Field()

    # Very unoptimized>__<
    @field_serializer('obj')
    def get_obj(self, _obj) -> Any:
        try:
            _val = app.ObjectsList.getByName(_obj.get('obj').get('saved_via').get('object_name'))

            return _val.getModule()(**_obj)
        except Exception as e:
            return _obj
