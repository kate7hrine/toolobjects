from App.Objects.Object import Object
from abc import abstractmethod

class Assertion(Object):
    @abstractmethod
    def check(self, argument: Object):
        ...
