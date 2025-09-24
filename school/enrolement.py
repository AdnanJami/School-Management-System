from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Enrolment(Base):
    __tablename__ = 'enrolments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    
    student = relationship("Student", back_populates="enrolments")
    course = relationship("Course", back_populates="enrolments")
    def __repr__(self):
        return f"<Enrolment(id={self.id}, student_id={self.student_id}, course_id={self.course_id})>"
    