from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime

class SegmentBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

class SegmentCreate(SegmentBase):
    pass

class SegmentUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

class SegmentOut(SegmentBase):
    id: int
    created_at: datetime

    # Pydantic v2 config for ORM support
    model_config = ConfigDict(from_attributes=True)

class AssignUsers(BaseModel):
    user_ids: List[int] = Field(..., min_items=1)

class AssignPercent(BaseModel):
    percentage: float = Field(..., gt=0.0, lt=100.0)

class UserOut(BaseModel):
    id: int
    segments: List[SegmentOut] = []

    # Pydantic v2 config for ORM support
    model_config = ConfigDict(from_attributes=True)
