from App.Objects.Mixins.BaseModel import BaseModel
from typing import Literal, Any

class Displayment(BaseModel):
    '''
    Class that display object some way
    '''

    role: list[Literal['str', 'js'] | str] = []
    value: str | Any = None # probaly module

    def implementation(self, i: dict) -> Any:
        '''
        The object to display is passed in i.get("object")
        '''

        orig = i.get('orig')

        return '0'
