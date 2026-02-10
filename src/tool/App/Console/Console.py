from App.Views.View import View
from App.Arguments.ArgumentsDict import ArgumentsDict
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Arguments.Assertions.InputNotInValues import InputNotInValues
from App.Arguments.Objects.Executable import Executable
from App.Logger.Log import Log

class Console(View):
    @staticmethod
    def printLog(to_print: Log = None):
        try:
            print(to_print.toStr())
        except Exception as e:
            print(e)

    async def implementation(self, i: dict = {}):
        executable = i.get('i')
        assert executable.meta.can_be_executed, 'cannot be executed'

        self.log(f"we gonna execute {executable}")

    @classmethod
    def getArguments(cls) -> ArgumentsDict:
        return ArgumentsDict.fromList([
            Executable(
                name = 'i',
                assertions = [
                    NotNoneAssertion(),
                    InputNotInValues(values=['App.Console.Console.Console'])
                ]
            )
        ])
