### App.Objects.Relations.Link

Link to another object instance.

#### Fields

|Field|Type|Description|
|--|--|--|
|item|Object instance|Item|
|data|[LinkData](./App.Objects.Relations.LinkData.md)|Info about link|

#### Related

* [App.Objects.Mixins.Linkable](./App.Objects.Mixins.Linkable.md)
* [App.Objects.Relations.LinkData](./App.Objects.Relations.LinkData.md)
* [App.Objects.Relations.LinkInsertion](./App.Objects.Relations.LinkInsertion.md)
* [App.Storage.Movement.Save](./App.Storage.Movement.Save.md)
* [App.DB.Link](./App.DB.Link.md)
* [App.DB.SwapLinks](./App.DB.SwapLinks.md)

#### Related settings

`app.db.linking.depth.default`: depth of recursion on links receivation when flushing into db. By default it's 29.
