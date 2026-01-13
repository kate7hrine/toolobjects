from App.Objects.Object import Object
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Threads.ExecutionThread import ExecutionThread
from Data.Dict import Dict
from pydantic import Field
from App import app

class List(Object):
    items: list[dict] = Field(default = [])

    @classmethod
    def mount(cls):
        autostarts = cls(
            items = []
        )

        for item in cls.getOption('app.autostart'):
            autostarts.items.append(item)

        app.mount('Autostart', autostarts)

    async def start_them(self, pre_i):
        self.log('Starting startup scripts')

        _iterator = 0

        _pre_i = pre_i()

        for item in self.items:
            thread = ExecutionThread(id = -1)
            thread.set_name('autostart_item ' + str(_iterator))
            thread.set(_pre_i.execute(item))

            app.ThreadsList.add(thread)

            await thread.get()

            _iterator += 1

    @classmethod
    def _settings(cls):
        return [
            ListArgument(
                name = 'app.autostart',
                default = [],
                orig = Dict,
            )
        ]
