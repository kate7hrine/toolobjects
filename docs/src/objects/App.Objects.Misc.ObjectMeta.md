### App.Objects.Misc.ObjectMeta

Description of object. Exist in every [Object](./App.Objects.Object.md) in the `obj` field. Values in these fields set by scripts, not manually.

#### Fields

|Field|Type|Description|
|-|-|-|
|name|`str`|Name of object|
|description|`str`|Description of object|
|collection|`bool`|Is this object is a collection? (should it be considered as such?)|
|role|`list[str]`||
|source|list of [Source](./App.Objects.Misc.Source.md)|Where did item come from? Author or original|
|created_at|`datetime`|When object was created? (means not an object instance)|
|updated_at|`datetime`|When object was updated?|
|dynamic_links|`bool`|Should dynamic links, if they are defined, be turned on or off?|
|saved_via|[SavedVia](#SavedVia)|
|width|`float`||
|height|`float`||
|duration|`float`||
|geo|`list`||

#### SavedVia

|Field|Type|Description|
|--|--|--|
|object_name|str|Name of object received by [`_getClassNameJoined()`](./App.Objects.Mixins.BaseModel.md)|
|created_by|str|Unused; but can be changed|
