from App.Objects.Object import Object
from App import app

class Storage(Object):
    @classmethod
    def mount(cls):
        storage = cls()

        app.mount('Storage', storage)
