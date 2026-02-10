### App.Objects.Extractor

Executable that returns list with objects. Basically, a wrapper around [ObjectsList](App.Objects.Responses.ObjectsList.md), it returns values from it.

The `_implementation()` function must return nothing, but itself it will return list with objects. The objects are added to response via `self.append()`.

The name is quite strong and it means that it should return something from other sources that should be saved or not saved yet.

There is `set_total_count` function that sets the common value of the objects from source.
