from App.Objects.Act import Act
from App.Objects.Object import Object
from typing import ClassVar, Any
from pydantic import Field
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone

class Thumbnail(Act):
    thumb_for: ClassVar[Any] = Object
    self_name = 'Thumbnail'

    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'object',
                orig = cls.thumb_for,
                #assertions = [NotNone()]
            )
        ])
