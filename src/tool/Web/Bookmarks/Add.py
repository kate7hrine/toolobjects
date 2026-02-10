from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from Data.Types.String import String
from Web.URL import URL
from Web.Bookmarks.Bookmarks import Bookmarks
from Web.Bookmarks.Bookmark import Bookmark
from App.Objects.Responses.ObjectsList import ObjectsList
from App.Storage.StorageUnitLink import StorageUnitLink
from App.Storage.StorageUnit import StorageUnit
from App import app

class Add(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            Argument(
                name = 'collection',
                by_id = True,
                orig = Bookmarks,
                assertions = [NotNone()]
            ),
            Argument(
                name = 'url',
                orig = URL,
                assertions = [NotNone()]
            ),
            Argument(
                name = 'title',
                orig = String,
                assertions = [NotNone()]
            ),
            Argument(
                name = 'favicon',
                orig = URL,
            ),
        ])

    async def _implementation(self, i):
        items = ObjectsList(items = [])
        unit = app.Storage.get('tmp').get_storage_adapter().get_storage_unit()

        favicon_url = i.get('favicon')
        collection = i.get('collection')
        item = Bookmark(
            url = i.get('url'),
        )
        item.obj.name = i.get('title')
        item.local_obj.make_public()

        if favicon_url:
            name = 'favicon.ico'
            _fav = app.DownloadManager.addURL(favicon_url, unit, name)
            await _fav.start()

            self.log('downloaded favicon')
            item.favicon = StorageUnitLink(
                path = name,
                insertion = item.link(unit).toInsert()
            )

        collection.link(item)

        item.save()

        items.append(item)

        return items
