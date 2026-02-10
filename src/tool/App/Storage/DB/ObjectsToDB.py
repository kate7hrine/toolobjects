from App.Objects.Executable import Executable
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Objects.List import List

class ObjectsToDB(Executable):
    @classmethod
    def getArguments(cls):
        return ArgumentDict(items=[
            List(
                name = 'models'
            )
        ])
