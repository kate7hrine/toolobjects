from App.Objects.Object import Object
from App.Objects.Executable import Executable
from pydantic import Field
from collections import deque

class ExecutablesList(Object):
    '''
    All running executables
    '''

    items: deque = Field()

    @classmethod
    def mount(cls):
        from App import app

        _objects = cls(
            items = deque()
        )

        app.mount('ExecutablesList', _objects)

    def add(self, item: Executable):
        self.items.append(item)

    def remove(self, item: Executable):
        if item in self.items:
            self.items.remove(item)
