from App.Objects.Object import Object
from App.Objects.Displayment import Displayment
from pydantic import Field

class Checkmark(Object):
    state: bool = Field(default = False)
    label: str = Field(default = None)

    @classmethod
    def getDisplayments(cls):
        class DisplayAsString(Displayment):
            role = ['str']

            def implementation(self, i):
                orig = i.get('orig')
                _mark = "[ ]"
                if orig.state:
                    _mark = "[x]"

                return _mark + " " + orig.label + ' ' # :((

        return [DisplayAsString()]
