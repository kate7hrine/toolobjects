from App.Objects.Act import Act
from datetime import datetime
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from Data.String import String
from Data.Boolean import Boolean
from App.Objects.Responses.ObjectsList import ObjectsList
from App.Storage.Item.Create import Create
from App.Storage.Item.PackToZip import PackToZip

class Export(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'items',
                assertions = [NotNoneAssertion()],
                orig = ObjectsList
            ),
            Argument(
                name = 'name',
                default = None,
                orig = String
            ),
            Argument(
                name = 'dir',
                orig = String
            ),
            Argument(
                name = 'as_zip',
                default = False,
                orig = Boolean
            ),
        ])

    async def implementation(self, i):
        export_name = i.get("name")
        if export_name == None:
            export_name = f"{int(datetime.now().timestamp())}_export"

        _create_items = await Create().execute({
            'name': export_name,
            'dir': i.get('dir')
        })
        export_storage = _create_items.items[0]

        for item in i.get('items').getItems():
            item.flush(export_storage)

        if i.get('as_zip') == True:
            await PackToZip().execute(i.change_for(PackToZip).update_values({
                'remove_dir': True
            }))

        return _create_items
