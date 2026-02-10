from App.Tests.Test import Test
from Data.Text import Text
from Data.Random import Random
from App import app

class FlushTest(Test):
    async def implementation(self, i):
        self.log('creating models')
        _id = Random().randomInt(0,1)

        items = [Text(text='123456'),Text(text='asdfghjkl')]

        _storage = app.Storage.get('content')
        _item = _storage.adapter.insertObject(items[_id])

        self.log(f'we saved object {_id} to id {_item.uuid}')
        self.log(f'getting object from db item')

        self.log(_item.getObject())
        self.log(_item.getObject().to_json())
