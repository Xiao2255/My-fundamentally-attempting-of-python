import json
from student import Student

def save_student(students:list[Student]) -> None:
    data = [{"name":student.name,
            "score":student.score} for student in students]
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(data,
                  f,
                  ensure_ascii=False,
                  indent=4,
                  )

def load_student() -> list[Student]:
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        students = [Student(item["name"],item["score"]) for item in data]
        return students

    except FileNotFoundError:
        return []

