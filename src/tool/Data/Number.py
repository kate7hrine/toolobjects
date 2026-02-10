from App.Objects.Object import Object
from App.Objects.Displayment import Displayment

class Number(Object):
    number: int | float = None

    @classmethod
    def getDisplayments(cls):
        class DisplayAsString(Displayment):
            role = ['str']

            def implementation(self, i):
                orig = i.get('orig')
                return str(orig.number)

        return [DisplayAsString()]
