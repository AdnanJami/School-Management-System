from pydantic import BaseModel

class EnrolmentBase(BaseModel):
    student_id: int
    course_id: int
class EnrolmentCreate(EnrolmentBase):
    pass
class EnrolmentResponse(EnrolmentBase):
    id: int
    class Config:
        from_attributes = True