from pydantic import BaseModel as PydanticBaseModel
from typing import Literal, ClassVar, Any

class Model(PydanticBaseModel):
    _unserializable: ClassVar[list[str]] = ['_dump_options', '_unserializable']

    # model_dump does not checks this params, so doing workaround. TODO remove
    _dump_options: ClassVar[dict] = {
        'convert_links': False,
        'include_extra': True,
        'excludes': None,
        'internal_fields': ['meta', 'saved_via', 'links', 'db_info'],
        'only_class_fields': False,
        'exclude_none': False,
        'exclude_defaults': False
    }

    # we can't use __init__ because of fields initialization, so we creating second constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__class__.init_hook(self)

    # *args and **kwargs are not passed
    def init_hook(self):
        pass

    def isInstance(self, object: PydanticBaseModel) -> bool:
        return self.getClassNameJoined() == object.getClassNameJoined()

    @classmethod
    def isSame(cls, object: PydanticBaseModel) -> bool:
        return cls.getNameJoined() == object.getNameJoined()

    @classmethod
    def getMRO(cls) -> list:
        return cls.__mro__

    @classmethod
    def canBeExecuted(cls):
        return hasattr(cls, 'execute')

    @classmethod
    def getClassName(cls):
        '''
        Path to the current class + class name:

        a.b.c.d.d or something
        '''

        return cls.getName() + [cls.getModuleName()]

    @classmethod
    def getModuleName(cls):
        return cls.__name__

    @classmethod
    def getNameJoined(self):
        return ".".join(self.getName())

    @classmethod
    def getClassNameJoined(cls, last_names_doubling: bool = False):
        '''
        getClassName() but joined
        '''

        _name = cls.getClassName()
        if last_names_doubling == False:
            _name = _name[:-1]

        return ".".join(_name)

    @classmethod
    def getName(self) -> list:
        _class = self.__mro__[0]
        _module = _class.__module__
        _parts = _module.split('.')
        #_parts = _parts[1:]

        return _parts

    @classmethod
    def getClassModule(cls) -> str:
        return cls.__module__

    @classmethod
    def getAllowedViews(cls) -> list:
        '''
        Get View classes where. if None > allowed everywhere
        '''
        return None
