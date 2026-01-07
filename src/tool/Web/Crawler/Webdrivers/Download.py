from App.Objects.Act import Act
from App.Objects.Object import Object
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.String import String
from App import app

class Download(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'driver',
                orig = Object,
                default = 'Web.Crawler.Webdrivers.Chromedriver.Download',
                assertions = [NotNoneAssertion()]
            )
        ], 
            missing_argument_inclusion = True
        )

    async def implementation(self, i):
        _driver = i.get('driver')

        return await _driver().execute(i)
