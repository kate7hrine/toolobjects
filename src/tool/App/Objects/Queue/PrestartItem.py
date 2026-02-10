from App.Objects.Queue.Item import Item
from App import app

class PrestartItem(Item):
    def get_orig(self):
        if type(self.predicate) == str:
            return app.ObjectsList.getByName(self.predicate).getModule()
