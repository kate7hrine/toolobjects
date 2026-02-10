from pydantic import Field
from App.Objects.Mixins.Model import Model
from typing import Optional

class SavedVia(Model):
    object_name: Optional[str] = Field(default = None)
    executable_name: Optional[str] = Field(default = None)
    # call_id: Optional[int] = Field(default = None)
