# 🏫 School Management System

A comprehensive school management system built with modern web technologies to streamline educational administration and management processes.

## 🚀 Tech Stack

- **Backend**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Language**: Python

## ✨ Features

- Student enrollment and management
- Teacher administration
- Course and curriculum management
- Grade tracking and reporting
- Administrative dashboard
- RESTful API architecture

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- PostgreSQL
- Git

## 🛠️ Installation

Follow these steps to set up the School Management System on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/AdnanJami/School-Management-System.git
```

### 2. Navigate to Project Directory

```bash
cd School-Management-System
```

### 3. Create Virtual Environment

```bash
python -m venv smsenv
```

### 4. Activate Virtual Environment

**On Windows:**
```bash
.\smsenv\Scripts\activate
```

**On macOS/Linux:**
```bash
source smsenv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Database Configuration

1. Open the `database.py` file in your preferred editor
2. Update the database credentials with your PostgreSQL configuration:

```python
# Example configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://username:password@localhost:5432/school_management"
    )
```

Make sure to replace:
- `username` with your PostgreSQL username
- `password` with your PostgreSQL password
- `localhost:5432` with your database host and port (if different)
- `school_management` with your desired database name

### 7. Database Setup

Create the database in PostgreSQL:

```sql
CREATE DATABASE school_management;
```
## Running Scraper
```bash
python scraper.py --pages {number of pages to scrap} {--db to save into database}
```
## 🚦 Running the Application

Start the development server:

```bash
uvicorn fast:app --reload
```

The application will be available at: `http://localhost:8000`

## 🔧 API Usage Examples

Here are some common API operations using PowerShell:

### Create a New Student

```powershell
Invoke-RestMethod -Method POST "http://localhost:8000/students" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{
    "name": "John Kobir",
    "email": "john.doe@email.com",
    "student_id": "ST001",
    "grade_level": 10
  }'
```

### Get Student by ID

```powershell
Invoke-RestMethod -Method GET "http://localhost:8000/students/1"
```

### Create a New Course

```powershell
Invoke-RestMethod -Method POST "http://localhost:8000/courses" `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{
    "name": "CSE332",
    "capacity": "32"
  }'
```

### Enroll Student to a Course

```powershell
Invoke-RestMethod -Method POST "http://localhost:8000/students/1/enrol/1"
```

### Import Scraped Data to Database

```powershell
Invoke-RestMethod -Method POST "http://localhost:8000/import/scraped"
```

### Get Scraped Resources from Database

```powershell
Invoke-RestMethod -Method GET "http://localhost:8000/scrapedresources"
```

### Alternative: Using cURL Commands

For cross-platform compatibility, you can also use cURL:

#### Create Student
```bash
curl -X POST "http://localhost:8000/students" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Kobir",
    "email": "john.doe@email.com",
    "student_id": "ST001",
    "grade_level": 10
  }'
```

#### Get Student by ID
```bash
curl -X GET "http://localhost:8000/students/1"
```

#### Create Course
```bash
curl -X POST "http://localhost:8000/courses" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "CSE332",
    "capacity": "32"
  }'
```

#### Enroll Student
```bash
curl -X POST "http://localhost:8000/students/1/enrol/1"
```

#### Import Scraped Data
```bash
curl -X POST "http://localhost:8000/import/scraped"
```

#### Get Scraped Resources
```bash
curl -X GET "http://localhost:8000/scrapedresources"
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Adnan Jami**

- GitHub: [@AdnanJami](https://github.com/AdnanJami)

## 🆘 Support

If you encounter any issues or have questions, please:

1. Check the existing [Issues](https://github.com/AdnanJami/School-Management-System/issues)
2. Create a new issue if your problem isn't already documented
3. Provide detailed information about your environment and the steps to reproduce the issue

## 🙏 Acknowledgments

- FastAPI team for the excellent framework
- SQLAlchemy team for the powerful ORM
- PostgreSQL team for the robust database system

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!# School-Management-System
This system is made with FastApi and sqlalchemy. PostgresSQL is being used as Database Server.

to use this First clone Github repository by typing 
git clone https://github.com/AdnanJami/School-Management-System.git
in you ternminal.
Type
cd .\School-Management-System\
Create Python Environment 
python -m venv smsenv

Initiate environment
.\smsenv\Scripts\activate
Install Dependencies
pip install -r requirement.txt
Edit database credentials in database.py
