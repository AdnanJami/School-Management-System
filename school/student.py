from models import Person
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
class Student(Person):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    student_id = Column(String, nullable=False, unique=True)
    grade_level = Column(Integer, nullable=True)
    enrolments = relationship("Enrolment", back_populates="student")
    
    def get_role(self):
        return "Student"
    def enrolled_courses(self):
        return [enrolment.course for enrolment in self.enrolments]
        