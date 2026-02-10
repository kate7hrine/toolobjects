from App.Objects.Act import Act
from App.Objects.Object import Object
from Data.Types.Int import Int
from Data.Types.String import String
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.AllowedValues import AllowedValues
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from App.Storage.StorageUUID import StorageUUID

class Link(Act):
    @classmethod
    def _arguments(cls):
        return ArgumentDict(items = [
            Argument(
                name = 'owner',
                orig = Object,
                by_id = True,
                assertions = [NotNone()]
            ),
            ListArgument(
                name = 'items',
                orig = Object,
                by_id = True,
                assertions = [NotNone()],
                default = []
            ),
            Argument(
                name = 'act',
                default = 'link',
                orig = String,
                values = AllowedValues(
                    values = ['link', 'unlink'],
                    strict = True
                )
            ),
            ListArgument(
                name = 'role',
                orig = String,
                assertions = [NotNone()],
                default = []
            ),
        ])

    async def _implementation(self, i):
        link_to = i.get('owner')
        _role = i.get('role')
        for item in i.get('items'):
            match (i.get('act')):
                case 'link':
                    link_to.link(item, _role)
                case 'unlink':
                    link_to.unlink(item, _role)

            self.log("{0}ed {1} and {2}".format(i.get('act'), link_to.getDbId(), item.getDbId()))
