from datetime import datetime

from pydantic import BaseModel


class IdentityModel(BaseModel):
    id: int


class MetaModel(BaseModel):
    created_at: datetime
    modified_at: datetime
