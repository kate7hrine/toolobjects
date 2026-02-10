from App.Objects.Locale.Documentation import Documentation
from App.Objects.Locale.Key import Key
from pydantic import Field

class ObjectDocumentation(Documentation):
    fields: dict[str, Key] = Field(default = {})
