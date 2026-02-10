from pydantic import Field, field_serializer
from datetime import datetime
from typing import Optional
from App.Objects.Mixins.Model import Model
from App.Objects.Misc.Source import Source
from App.Objects.Misc.SavedVia import SavedVia

class ObjectMeta(Model):
    saved_via: SavedVia = Field(default = None)

    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    collection: Optional[bool] = Field(default=False)
    role: Optional[list[str]] = Field(default = [])

    source: list[Source] = Field(default = [], repr = False)

    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = Field(default=None)

    # other fields
    width: Optional[int] = Field(default = None)
    height: Optional[int] = Field(default = None)
    duration: Optional[int] = Field(default = None)

    def set_common_source(self, source: Source):
        source.is_common = True

        self.source.append(source)

    def add_source(self, source: Source):
        self.source.append(source)

    def get_common_source(self):
        for source in self.source:
            if source.is_common == True:
                return source
