from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from App.Objects.ScheduledTasks.Task import Task
from App import app

class Add(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'task',
                orig = Task,
                by_id = True,
                assertions = [NotNone()]
            )
        ])

    def _implementation(self, i):
        task = i.get('task')
        task.flush(app.Storage.get('scheduled_tasks'), set_db_if_set = True)
        task.save()
