from App.DB.Adapters.ConnectionAdapter import ConnectionAdapter
from App.DB.Adapters.Search.Query import Query
from App.DB.Adapters.Representation.ObjectAdapter import ObjectAdapter
from App.DB.Adapters.Representation.LinkAdapter import LinkAdapter
from pydantic import Field

class ObjectsList(ConnectionAdapter):
    protocol_name = 'objects_list'
    file: str = Field()

    def _init_models(self_adapter):
        class ObjectAdapter(ObjectAdapter):
            pass
        
    def _constructor(self):
        connection_string = self.protocol_name + self.delimiter + self.getConnectionStringContent()

        self._set_id_gen()
        self._init_models()
