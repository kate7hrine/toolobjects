from Data.JSON import JSON
from App import app
from typing import Any

class ObjectAdapter():
    '''
    Transition class between App.Objects.Object and SQL

    must contain uuid and content
    '''

    def getById(self, id: int):
        pass

    def _constructor(self, storage_item: Any = None):
        pass

    def getObject(self):
        _content = JSON().fromText(self.content)
        _object_name = _content.data.get('saved_via').get('object_name')
        _class = app.ObjectsList.getByName(_object_name).getModule()
        _item = _class.model_validate(_content.data, strict = False)
        _item.setDb(self)

        return _item
