import csv
from pathlib import Path
from student import Student

def load_students(file_path):
    students = []
    with Path(file_path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks = [float(row["mark1"]), float(row["mark2"]), float(row["mark3"])]
            students.append(Student(row["sap_id"], row["name"], marks))
    return students

def save_student_report(student, file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with Path(file_path).open("w", encoding="utf-8") as f:
        f.write(f"SAP ID: {student.sap_id}\nName: {student.name}\nAverage: {student.calculate_average():.2f}\nGrade: {student.calculate_grade()}\n")

def main():
    try:
        students = load_students("week04/data/students.csv")
        for s in students:
            print(s.format_profile())
            save_student_report(s, f"week04/reports/{s.sap_id}.txt")
    except FileNotFoundError:
        print("Student data file was not found in week04/data.")
    except ValueError as e:
        print(f"Invalid student data: {e}")

if __name__ == "__main__":
    main()