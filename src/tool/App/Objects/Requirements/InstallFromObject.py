from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Objects.Arguments.Argument import Argument
from App.Objects.Executable import Executable
from App.Objects.Requirements.Install import Install

class InstallFromObject(Act):
    @classmethod
    def _arguments(cls):
        return ArgumentDict(items=[
            Argument(
                name = 'object',
                orig = Executable,
                assertions = [NotNoneAssertion()]
            )
        ])

    async def implementation(self, i):
        _object = i.get('object')
        _requirements = _object.getNotInstalledModules()
        if len(_requirements) < 1:
            self.log(f"plugin {_object.getNameJoined()} does not contains uninstalled modules")
        else:
            await Install().execute({
                'requirements': _requirements
            })
