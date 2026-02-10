from App.Objects.Object import Object
from pydantic import Field
from typing import Any, ClassVar

class ConnectionAdapter(Object):
    '''
    Adapter for some object store (for example, db)
    '''

    protocol_name: ClassVar[str] = ''

    protocol: str = Field(default = 'none')
    delimiter: str = Field(default = ':///')
    name: str = Field(default = 'units')

    ObjectAdapter: Any = None
    ObjectLinkAdapter: Any = None

    def flush(self, item: Object):
        pass
