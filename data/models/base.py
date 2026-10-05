from datetime import datetime

from pydantic import BaseModel


class IdentityModel(BaseModel):
    id: int



class TimestampModel(BaseModel):
    created_at: datetime
    modified_at: datetime

class AttributionModel(BaseModel):
    created_by: int
    modified_by: int

class AuditModel(TimestampModel, AttributionModel):
    pass
