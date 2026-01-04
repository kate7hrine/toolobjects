from App.Objects.Object import Object
from typing import ClassVar
from pydantic import Field
from App import app

class Path(Object):
    root: str = Field()
    parts: list[str | int] = Field(default = [])
    divider: str = '/'
    connection_divider: ClassVar[str] = ':/'

    @staticmethod
    def from_str(str: str):
        _root_and_other = str.split(Path.connection_divider)
        _path = Path(root = _root_and_other[0])

        _paths = _root_and_other[1]
        if len(_paths) > 0:
            for item in _paths.split(_path.divider):
                _path.parts.append(item)

        return _path

    def get_root(self):
        _root = self.root

        return app.Storage.get(_root)

    def to_args(self) -> dict:
        root_name = self.root
        root = self.get_root()
        cursor = None

        if len(self.parts) == 0:
            _root_uuid = root.root_uuid
            if _root_uuid != None:
                return {
                    'linked_to': root_name + '_' + _root_uuid
                }
            else:
                self.log('root_uuid is None, so returning everything')

                return {}

        for part in self.parts:
            if len(part) == 0:
                return {
                    'linked_to': root_name + '_' + cursor
                }

            cursor = part

        return {
            'uuids': [root_name + '_' + cursor]
        }
