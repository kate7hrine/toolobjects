from App.Objects.Mixins.Model import Model
from typing import Literal
from pydantic import Field, field_serializer
from App.Objects.Index.ModuleData import ModuleData
from App import app
from typing import Any

class Submodule(Model):
    item: str | Any = Field()
    role: list[Literal['link_allowed', 'usage', 'action', 'object_in', 'object_out', 'object', 'thumbnail', 'thumbnail_disabled_default', 'common', 'wheel', 'convertation', 'test', 'returns', 'allowed_view'] | str] = Field(default = ['common'])

    def getItem(self):
        if type(self.item) == str:
            _module = app.ObjectsList.getByName(self.item)
            return _module.getModule()
        else:
            return self.item

    # ???
    @field_serializer('item')
    def get_item(self, item) -> str:
        if item == None:
            return None

        return ModuleData.from_module(item)
