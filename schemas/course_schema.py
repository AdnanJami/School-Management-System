from pydantic import BaseModel, field_validator
from typing import Optional

class CourseBase(BaseModel):
    name: str
    capacity: int
    teacher_id: Optional[int] = None
    @field_validator('capacity')
    @classmethod
    def validate_capacity(cls, v):
        if v < 1 or v > 500:
            raise ValueError("Capacity must be a positive integer")
        return v
    
class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int  
    available_seats: int
    class Config:
        from_attributes = True