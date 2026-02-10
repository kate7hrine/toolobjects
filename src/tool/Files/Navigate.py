from App.Objects.Act import Act
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Types.String import String
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Responses.AnyResponse import AnyResponse
from pathlib import Path

from Files.File import File

class Navigate(Act):
    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items=[
            String(
                name = 'path',
                assertions = [
                    NotNoneAssertion()
                ]
            )
        ])

    async def implementation(self, i):
        _path = Path(str(i.get('path')))
        _item = File.fromPath(_path)

        return AnyResponse(
            data = _item.file.getContent()
        )
