from App.Objects.Link import Link
from Data.JSON import JSON

class ObjectLinkAdapter():
    '''
    must contain: uuid, owner, target and roles
    '''

    def getById(self, id: int):
        pass

    def getLink(self):
        _role = JSON().fromText(self.role)

        _link = Link(item = None)
        _link.item = self.getTarget().getObject()
        _link.role = _role
        _link.setDb(self)

        return _link
