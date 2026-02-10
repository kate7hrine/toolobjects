from App.Objects.Arguments.ArgumentDict import ArgumentDict
from pydantic import Field

class Validable:
    '''
    Mixin that contains function with arguments lists that can be used for validation
    '''

    def getCompareKeys(self) -> list:
        _keys = list()
        for item in self.getArguments().toList():
            _keys.append(item.name)

        return _keys

    @classmethod
    def _arguments(cls) -> ArgumentDict:
        '''
        Arguments for validation
        '''
        return ArgumentDict(items = [])

    @classmethod
    def getArguments(cls) -> ArgumentDict:
        '''
        Joins ArgumentDicts from all extended classes
        '''

        # Takes current ArgumentDict
        _list = cls._arguments()

        # Slicing current class
        for _class in cls.getMRO()[1:]:
            if hasattr(_class, '_arguments'):
                new_arguments = _class._arguments()
                if new_arguments == None:
                    continue

                _list.join(new_arguments)

        return _list
