from pydantic import Field
from App.Objects.Mixins.Model import Model
from .SavedVia import SavedVia
from typing import Optional
from datetime import datetime
from .Thumbnail import Thumbnail

class LocalObjectMeta(Model):
    saved_via: Optional[list[SavedVia]] = Field(default = [])

    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)

    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    edited_at: Optional[datetime] = Field(default=None)

    public: Optional[bool] = Field(default=False)
    role: Optional[list[str]] = Field(default = [])
    thumbnail: Optional[list[Thumbnail]] = Field(default = [])

    def add_thumbnail(self, thumb: Thumbnail):
        self.thumbnail.append(thumb)

    def add_thumbnails(self, thumbs: list[Thumbnail]):
        for thumb in thumbs:
            self.thumbnail.append(thumb)

    def make_public(self):
        self.public = True
