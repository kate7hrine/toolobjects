from App.Objects.Object import Object
from App.Storage.StorageUUID import StorageUUID
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Daemons.DaemonItem import DaemonItem
from pydantic import Field
from App import app

class List(Object):
    autostart: list[DaemonItem] = Field(default = [])

    @classmethod
    def mount(cls):
        daemons = cls(
            items = []
        )

        for item in cls.getOption('app.daemons.autostart'):
            try:
                daemons.autostart.append(item.get_item().toPython())
            except AttributeError:
                daemons.log_error('item {0} does not exists'.format(item.item.getId()))

        app.mount('DaemonList', daemons)

    @classmethod
    def _settings(cls):
        return [
            ListArgument(
                name = 'app.daemons.autostart',
                default = [],
                orig = DaemonItem,
            )
        ]
