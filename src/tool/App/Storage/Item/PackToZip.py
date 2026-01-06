from App.Objects.Act import Act
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument

class PackToZip(Act):
    '''
    Packs StorageItem to zip
    '''

    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'item',
            )
        ])
