from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("Teacher", back_populates="courses")
    enrolments = relationship("Enrolment", back_populates="course")
    
    def is_full(self):
        return len(self.enrolments) >= self.capacity
    
    def count_available_seats(self):
        return self.capacity - len(self.enrolments)
    
from school.teacher import Teacher
from school.enrolement import Enrolment