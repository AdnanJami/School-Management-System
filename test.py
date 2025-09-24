import pytest
from enrolement_service import EnrolmentService
from database import DBSession
from school.student import Student
from school.course import Course

def test_enrolement_service(db_session):
    studen1 = Student(name="Alice",email="john.doe@email.com",student_id="ST001")
    student2 = Student(name="Bob",email="bob.doe@email.com",student_id="ST002")
    db_session.add_all([studen1,student2])
    db_session.commit()
    course1 = Course(name="Math 101",capacity=40)
    course2 = Course(name="History 101",capacity=30)
    db_session.add_all([course1,course2])
    db_session.commit()
    service = EnrolmentService(db_session)
    assert service is not None
    enrol = service.enrol_student(studen1.id, course1.id)
    assert enrol is not None
    assert enrol.student_id == studen1.id
    assert enrol.course_id == course1.id

def prevent_duplicate_enrolment(db_session):
    student = Student(name="Jami",email="jami@gmail.com",student_id="ST003")
    course = Course(name="Science 101",capacity=25)
    db_session.add_all([student,course])
    db_session.commit()
    service = EnrolmentService(db_session)
    assert service is not None
    enrol = service.enrol_student(student.id, course.id)
    assert enrol is not None
    
    with pytest.raises(ValueError) as excinfo:
        service.enrol_student(student.id, course.id)
    assert "already enrolled" in str(excinfo.value)
    
def test_course_capacity_limit(db_session):
    """Test course capacity enforcement"""
    # Create course with capacity of 1
    course = Course(
        course_code="CS103",
        capacity=1
    )
    
    db_session.add(course)
    db_session.commit() 
    
    student1 = Student(
        name="Student One",
        email="student1@email.com",
        student_id="ST007"
    )
    student2 = Student(
        name="Student Two",
        email="student2@email.com",
        student_id="ST008"
    )
    db_session.add_all([student1,student2])
    db_session.commit() 
    service = EnrolmentService(db_session)
    assert service is not None
    enrol1 = service.enrol_student(student1.id, course.id)
    assert enrol1 is not None
    with pytest.raises(ValueError) as excinfo:
        service.enrol_student(student2.id, course.id)
    
    
