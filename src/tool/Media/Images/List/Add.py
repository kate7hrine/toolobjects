from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.ListArgument import ListArgument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from Media.Images.List.List import List
from Media.Media import Media

class Add(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'list',
                orig = List,
                assertions = [NotNone()]
            ),
            ListArgument(
                name = 'images',
                orig = Media,
                id_allow = True,
                assertions = [NotNone()]
            )
        ])

    def implementation(self, i):
        gallery = i.get('list')
        images = i.get('images')

        for image in images:
            gallery.link(image)
