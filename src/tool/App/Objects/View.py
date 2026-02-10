from App.Objects.Executable import Executable
from typing import Any
from App.App import App
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone

class View(Executable):
    '''
    Wrapper of the app. Contains executable interface that runs from tool.py
    '''

    app: Any = None

    def _implementation(self, i):
        # the default View is created at the startup, but it will throw an abstract method exception if no dummy func
        pass

    def setApp(self, app: App) -> None:
        self.app = app

    def setAsCommon(self):
        from App import app

        app.setView(self)

    def canUseObject(self, obj) -> bool:
        if obj.isInstance(View):
            return False

        _allowed = obj._allowed_views()
        if _allowed == None:
            return True

        for item in _allowed:
            if item._getClassNameJoined() == self._getClassNameJoined():
                return True

    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'pre_i',
                orig = Executable,
                default = 'App.Objects.Operations.DefaultExecutorWheel',
                assertions = [
                    NotNone()
                ]
            ),
        ])
