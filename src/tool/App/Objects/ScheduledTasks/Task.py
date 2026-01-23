from App.Objects.Object import Object
from pydantic import Field
from datetime import datetime
from App.Objects.Autostart.Item import Item

class Task(Item):
    run_at: datetime = Field()
