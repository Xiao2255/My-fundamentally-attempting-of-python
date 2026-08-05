import json
from student import Student

def save_student(students):
    data = []
    for student in students:
        data.append({
            "name":student.name,
            "score":student.score
    })
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data,
                  f,
                  ensure_ascii=False,
                  indent=4,
                  )

def load_student():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        students = []

        for item in data:
            student = Student(item["name"],item["score"])
            students.append(student)
        return students

    except FileNotFoundError:
        return []

