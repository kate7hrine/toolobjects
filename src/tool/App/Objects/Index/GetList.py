from App.Objects.Act import Act
from App.Objects.Responses.ObjectsList import ObjectsList
from App import app

class GetList(Act):
    def implementation(self, i):
        _items = ObjectsList()
        for item in app.ObjectsList.getItems().toList():
            _items.append(item)

        return _items
