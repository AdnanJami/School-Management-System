from models import Person
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Teacher(Person):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    employee_id = Column(String, nullable=False, unique=True)
    department = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")
    
    def get_role(self):
        return "Teacher"
    
    def course_count(self):
        return len(self.courses)
    
    def get_courses(self):
        return [course.name for course in self.courses]
    
