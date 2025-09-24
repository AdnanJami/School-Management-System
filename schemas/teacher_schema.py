from pydantic import BaseModel,EmailStr, field_validator
from typing import Optional 

class TeacherBase(BaseModel):
    name: str
    email: EmailStr
    employee_id: str
    department: str
    @field_validator('employee_id')
    @classmethod
    def validate_employee_id(cls, v):
        if len(v) < 5:
            raise ValueError("Employee ID must be at least 5 characters long")
        return v
    
class TeacherCreate(TeacherBase):
    pass

class TeacherResponse(TeacherBase):
    id: int
    course_count: Optional[int] = 0
    
    class Config:
        from_attributes = True
    
    
    