from App.Objects.Object import Object
from App.Objects.Displayment import Displayment
from App.Objects.Relations.LinkInsertion import LinkInsertion
from Data.String import String
from pydantic import Field

class Checkmark(Object):
    state: bool = Field(default = False)
    label: String | LinkInsertion = Field(default = None)

    @classmethod
    def getDisplayments(cls):
        class DisplayAsString(Displayment):
            role = ['str']

            def implementation(self, i):
                orig = i.get('orig')
                _mark = "[ ]"
                if orig.state:
                    _mark = "[x]"

                # TODO remove
                _i = orig.to_json()
                return _mark + " " + _i.get('label').get('value') + ' ' # :((

        return [DisplayAsString()]
