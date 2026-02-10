from pydantic import BaseModel, ConfigDict

class AllowExtraFields(BaseModel):
    model_config = ConfigDict(extra='allow')
