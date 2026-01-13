from App.Objects.Act import Act
from App.Objects.Index.ObjectsList import ObjectsList
from App.Objects.Responses.AnyResponse import AnyResponse
from App import app

class ReloadAll(Act):
    def _implementation(self, i):
        for namespace in app.ObjectsList.namespaces:
            namespace.unload()

        ObjectsList.mount()

        return AnyResponse(data = True)
