from pydantic import Field
from App.Objects.Mixins.Model import Model
from typing import Optional

class SavedVia(Model):
    object_name: Optional[str] = Field(default = None)
    created_by: Optional[list[str]] = Field(default = None)
