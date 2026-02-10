from App.Objects.Executable import Executable
from App.Arguments.ArgumentsDict import ArgumentsDict
from typing import Any
from App.App import App

class View(Executable):
    '''
    Wrapper of the app. Contains executable interface that runs from tool.py
    '''

    app: Any = None

    def setApp(self, app: App) -> None:
        self.app = app

    def setAsCommon(self):
        '''
        Sets link that can be used as

        from App import app

        app.Logger.log(...)
        '''
        from App import app

        app.setView(self)

    def implementation(self, i: ArgumentsDict = {}):
        pass
