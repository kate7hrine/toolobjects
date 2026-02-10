### App.Objects.Relations.Submodule

Describes the link to another object.

#### Fields

|Field|Type|Description|
|--|--|--|
|item|Class|Link to the class|
|role|`list[str]`|Description of the relation towards this class|

**Roles table**

`role` list can contain any strings, but there is roles that defined in the app:

|Role|Description|What does it do?|Where is it used?|
|--|--|--|--|
|link_allowed|Items with `item` class can be linked to this class|❌|❌|
|returns|Objects with `item` class will be returned|❌|❌|
|allowed_view|Object can be executed only when [View](./App.Objects.View.md) is an `item`|If current view is not in submodules with role "allowed_view", it won't run|DefaultExecutorWheel|
|usage|`item` is used inside `_implementation()` of this class|Arguments from `item` are applying to the result of `getArguments()` function if `include_usage` is True|Validable|
|action|`item` is an action that somehow related to this class|❌|Client|
|object|`item` is an object that somehow related to this class|❌|Client|
|common|`item` is an object that related to this class and is common to it (?)|❌|Client|
|wheel|-|`item` will be used in Wheel|Wheel|
|thumbnail|-|`item` will be used as thumbnail creation mechanism|Media|
|thumbnail_disabled_default|-|`item` will be used as thumbnail creation mechanism, but it will be disabled by default|Media|
|object_in|The object to be converted|Defines class that will be used for convertation|Convertations|
|object_out|The object to be converted into|Defines class that passed object will be converted into|Convertations|
|convertation|-|`item` will be shown in convertation list|Convertations|
|test|`item` is a test of this class|❌|❌|

#### Serialization

Because classes cannot be serialized to json, they returns as [ModuleData](./App.Objects.Index.ModuleData.md).

#### Related

* [App.Objects.Mixins.Submodulable](./App.Objects.Mixins.Submodulable.md)
