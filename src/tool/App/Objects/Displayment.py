from App.Objects.Executable import Executable
from App.Objects.Object import Object
from typing import Literal, ClassVar, Any

class Displayment(Executable):
    '''
    Class that display object some way
    '''

    role: ClassVar[list[Literal['str', 'js'] | str]] = []

    def implementation(self, i: dict) -> Any:
        '''
        The object to display is passed in i.get("object")
        '''

        orig = i.get('orig')

        return '0'
