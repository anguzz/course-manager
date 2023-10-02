import sqlite3
from schemas import Class, Student, Department, Instructor#, Registrar

sample_classes = [
    Class(
        id=1,
        department= Department(id=1, name="CPSC"),
        course_code="449",
        section_number="001",
        name="Web Back-End Engineering",
        instructor= Instructor(id=1, name="Kennyt Avery"),
        current_enroll=25,
        max_enroll=30,
    ),
     Class(
        id=2,
        department= Department(id=1, name="CPSC"),
        course_code="349",
        section_number="233430",
        name="Web Front-End Engineering",
        instructor= Instructor(id=1, name="Kennyt Avery"),
        current_enroll=25,
        max_enroll=30,
    ),
    Class(
        id=3,
        department= Department(id=1, name="CPSC"),
        course_code="120",
        section_number="1344",
        name="Introduction to Computer Science",
        instructor= Instructor(id=2, name="Prof. Smith"),
        current_enroll=45,
        max_enroll=50,
    ),
    Class(
        id=4,
        department= Department(id=2, name="MATH"),
        course_code="150",
        section_number="002",
        name="Calculus I",
        instructor=Instructor(id=3, name="Prof. Johnson"),
        current_enroll=30,
        max_enroll=40,
    ),
    Class(
        id=5,
        department= Department(id=3, name="ENGL"),
        course_code="101",
        section_number="003",
        name="Composition and Rhetoric",
        instructor=Instructor(id=4, name="Prof. Davis"),
        current_enroll=20,
        max_enroll=25,
    ),
    Class(
        id=6,
        department= Department(id=4, name="PHYS"),
        course_code="210",
        section_number="004",
        name="Physics I",
        instructor=Instructor(id=5, name="Kennyt Adams"),
        current_enroll=28,
        max_enroll=30,
    ),
    Class(
        id=7,
        department= Department(id=5, name="CHEM"),
        course_code="220",
        section_number="005",
        name="Chemistry II",
        instructor=Instructor(id=6, name="Prof. Miller"),
        current_enroll=22,
        max_enroll=25,
    ),
    Class(
        id=8,
        department= Department(id=6, name="HIST"),
        course_code="402",
        section_number="03",
        name="Reading Seminar",
        instructor=Instructor(id=7, name="Prof. Washington"),
        current_enroll=26,
        max_enroll=30,
    ),
    Class(
        id=9,
        department= Department(id=7, name="BIO"),
        course_code="312",
        section_number="045",
        name="Marine Biology",
        instructor=Instructor(id=8, name="Prof. Emily"),
        current_enroll=31,
        max_enroll=33,
    ),
    Class(
        id=10,
        department= Department(id=8, name="BUSI"),
        course_code="380",
        section_number="125",
        name="Business Thinking",
        instructor=Instructor(id=9, name="Prof. Arvizu"),
        current_enroll=60,
        max_enroll=62,
    ),
]

sample_students = [
    Student(name="homer simpson", id="ab34223"),
    Student(name="Philly J. Fry", id="D3456"),
    Student(name="Angel Santoyo", id="LB23456"),
    Student(name="David Carlson", id="A23456"),
    Student(name="John Smith", id="J23456"),
    Student(name="Steve Smith", id="Pf3456"),
    Student(name="Bob Taylor", id="Bf3456"),
    Student(name="Joe Schmoe", id="Af3456"),
    Student(name="Dwanye Johnson", id="8SD2SM2"),
    Student(name="John Cena", id="9ce8FJ1"),
]
"""
sample_registrar = [
    Registrar(name="John Smith", registar_id ="1")
]
"""
# populates db
def populate_database():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        for class_data in sample_classes:
            cursor.execute(
                """
                INSERT INTO classes (department, course_code, section_number, name, instructor, current_enrollment, max_enrollment)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    class_data.department,
                    class_data.course_code,
                    class_data.section_number,
                    class_data.name,
                    class_data.instructor,
                    class_data.current_enroll,
                    class_data.max_enroll,
                ),
            )

        for student_data in sample_students:
            cursor.execute(
                """
                INSERT INTO students (name, student_id)
                VALUES (?, ?)
                """,
                (student_data.name, student_data.id),
            )

        conn.commit()
        cursor.close()
        conn.close()

        print("Database populated :D")

    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    populate_database()
