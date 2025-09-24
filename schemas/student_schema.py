from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class StudentBase(BaseModel):
    name: str
    email: EmailStr
    student_id: str
    grade_level: Optional[int] = None

    @field_validator('grade_level')
    @classmethod
    def validate_grade_level(cls, v):
        if v is not None and (v < 1 or v > 12):
            raise ValueError("Grade level must be between 1 and 12")
        return v

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int  

    class Config:
        from_attributes = True  