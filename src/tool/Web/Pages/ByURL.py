from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from Data.String import String
from Web.Crawler.Webdrivers.Webdriver import Webdriver

class ByURL(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'url',
                orig = String,
                assertions = [NotNoneAssertion()]
            ),
            Argument(
                name = 'webdriver',
                orig = Webdriver,
                id_allow = True,
                assertions = [NotNoneAssertion()]
            )
        ])

    async def implementation(self, i):
        url = i.get('url')

        print(url)
