### App.Objects.Misc.LocalObjectMeta

Similar to [ObjectMeta](./App.Objects.Misc.ObjectMeta.md), but contains changeable data. Exists in `local_obj` field.

#### Fields

|Field|Type|Description|
|-|-|-|
|name|`str`|Name of object|
|description|`str`|Description of object|
|collection|`bool`|Is this object is a collection? (should it be considered as such?)|
|created_at|`datetime`|When the object instance was created|
|edited_at|`datetime`|When the object instance was edited?|
|updated_at|`datetime`|When the object instance was edited or linked|
|geo|list of Geo|-|
|public|`bool`|Is object is not unlisted? It must be True only when object is for internal use.|
|thumbnail|list of Thumbnail|Object's thumbnails|
