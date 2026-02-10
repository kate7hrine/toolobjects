from pydantic import BaseModel

class Convertable(BaseModel):
    @classmethod
    def findConvertationsForClass(cls, for_class: BaseModel) -> list:
        # wtf ...
        converters = []
        for submodule in cls.getAllSubmodules(with_role=['convertation']):
            obj_in = submodule.item.getAllSubmodules(with_role=['object_out'])
            for _submodule in obj_in:
                if _submodule.item is for_class:
                    converters.append(submodule)

        return converters

    async def convertTo(self, to_class: BaseModel):
        _itms = self.findConvertationsForClass(to_class)
        _conv = _itms[0]

        assert _conv != None, 'no convertation for this'

        _itm = _conv.item()
        return await _itm.execute(i = {'orig': self})
