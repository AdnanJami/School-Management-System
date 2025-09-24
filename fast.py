from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI,HTTPException
import json
from scraper import save_to_db
from schemas.student_schema import StudentBase, StudentCreate, StudentResponse
from schemas.teacher_schema import TeacherBase, TeacherCreate, TeacherResponse
from schemas.course_schema import  CourseCreate, CourseResponse
from schemas.enrolement_schemas import  EnrolmentResponse
from scemas import BookResponse
from school.student import Student
from school.course import Course
from school.teacher import Teacher
from school.enrolement import Enrolment
from database import engine, Base, DBSession
from models import Book
Base.metadata.create_all(bind=engine)
from enrolement_service import EnrolmentService
app = FastAPI()
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/import/scraped")
def import_json():
    try:
        print("Starting import...")
        
        print("Opening file...")
        with open("samples/scraped.json", "r", encoding="utf-8") as f:
            print("Loading JSON...")
            data = json.load(f)
            print(f"Loaded {len(data)} items")
            
            print("Saving to database...")
            save_to_db(data)
            
            print("Import completed successfully")
            return {
                "message": "Successfully imported items",
            }
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise HTTPException(status_code=404, detail="scraped.json file not found")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        raise HTTPException(status_code=400, detail="Invalid JSON format")
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Import failed: {str(e)}")

@app.get("/scraped",response_model=list[BookResponse])
def get_scraped():
    try:
        with open("samples/scraped.json", "r",encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Scraped data file not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error reading scraped data")
@app.get("/scrapedresources",response_model=list[BookResponse])
def get_scraped_resources(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
@app.get("/students/", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    if db.query(Student).filter_by(email=student.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(Student).filter_by(student_id=student.student_id).first():
        raise HTTPException(status_code=400, detail="Student ID already exists")
    db_student = Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter_by(id=student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.post("/students/{student_id}/enrol/{course_id}")
def enrol_student(student_id: int, course_id: int):
    try:
        service= EnrolmentService()
        enrolment = service.enrol_student(student_id, course_id)
        return {"message": "Student enrolled successfully", "enrolment_id": enrolment.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/courses/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if db.query(Course).filter_by(name=course.name).first():
        raise HTTPException(status_code=400, detail="Course name already exists")
    db_course = Course(**course.model_dump())
    
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    db_course.available_seats = db_course.count_available_seats()
    return db_course

@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(Course).filter_by(id=course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    db_course.available_seats = db_course.count_available_seats()
    return db_course

@app.get("/courses/", response_model=list[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    for course in courses:
        course.available_seats = course.count_available_seats()
    return courses

@app.post("teacher/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    if db.query(Teacher).filter_by(email=teacher.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(Teacher).filter_by(employee_id=teacher.employee_id).first():
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    db_teacher = Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher
@app.get("/teacher/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter_by(id=teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_teacher.course_count = len(db_teacher.courses)
    return db_teacher
@app.get("/student/{student_id}/enrolments/", response_model=EnrolmentResponse)
def get_student_enrolments(student_id: int):
    enrolments = EnrolmentService.get_student_enrolments(student_id)
    return enrolments
@app.get("/course/{course_id}/enrolments/", response_model=list[EnrolmentResponse])
def get_course_enrolments(course_id: int):
    enrolments = EnrolmentService.get_course_enrolments(course_id)
    return enrolments