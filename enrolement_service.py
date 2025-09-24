
from school.student import Student
from school.course import Course
from school.enrolement import Enrolment
from sqlalchemy.orm import Session
class EnrolmentService:
    def __init__(self, db_session = Session):
        self.db_session = db_session
        
    def enrol_student(self, student_id: int, course_id: int):
        student = self.db_session.query(Student).filter_by(id=student_id).first()
        course = self.db_session.query(Course).filter_by(id=course_id).first()
        if not student or not course:
            raise ValueError("Invalid student or course ID")
        if self.db_session.query(Enrolment).filter_by(student_id=student_id, course_id=course_id).first():
            raise ValueError("Student already enrolled in this course")
        if course.is_full():
            raise ValueError("Course is full")
        enrolment = Enrolment(student_id=student_id, course_id=course_id)
        self.db_session.add(enrolment)
        self.db_session.commit()
        return enrolment

    def get_student_enrolments(self, student_id: int):
        enrolments = self.db_session.query(Enrolment).filter_by(student_id=student_id).all()
        return enrolments

    def get_course_enrolments(self, course_id: int):
        enrolments = self.db_session.query(Enrolment).filter_by(course_id=course_id).all()
        return enrolments
