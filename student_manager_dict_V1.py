import json


def save_student(students):
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students,
                  f,
                  ensure_ascii=False,
                  indent=4,
                  )

def load_student():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)
        return students

    except FileNotFoundError:
        return []

students = load_student()


def add_student(students):
    name = input("请输入学生姓名：")
    for student in students:
        if student["name"] == name:
            print("该名字已添加！")
            return

    while True:
        try:
            score = int(input("请输入学生成绩："))
            if 0<=score<=100:
                print("添加成功！")
                break
            else:
                print("请输入正确数字！")
        except ValueError:
            print("请输入数字！")
    student ={"name":name,"score":score}
    students.append(student)

def show_students(students):
    for student in students:
        result = judge_score(student["score"])
        print(f'\n{student["name"]}的成绩为{student["score"]}，等级为：{result}')

def average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    avg = total / len(students)
    max_score = students[0]["score"]
    min_score = students[0]["score"]
    max_student = students[0]["name"]
    min_student = students[0]["name"]
    for student in students:
            if student["score"] > max_score:
                max_student = student["name"]
                max_score = student["score"]
            if  student["score"] < min_score:
                min_student = student["name"]
                min_score = student["score"]
    print(f'全班的平均分为：{avg}，其中，全班最高分为：{max_student},是{max_score};最低分为：{min_student}, {min_score}')

def find_student(students):
    name = input("请输入需要查找学生的名字：")
    found = False
    for student in students:
        if name in student["name"]:
         print(f'{student["name"]}的成绩为：{student["score"]}')
         found = True
    if not found:
            print("暂无该学生信息！")

def delete_student(students):
    name = input("请输入需要删除学生的姓名：")
    found = False
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("删除成功！")
            found = True
            break
    if not found:
            print("暂无该学生信息！")

def update_student(students):
    name = input("请输入需要更新成绩的学生的姓名：")
    new_score = int(input("请输入更新后的成绩："))
    found = False
    for student in students:
        if student["name"] == name:
            student["score"] = new_score
            print(f'修改成功！{name}当前的新成绩为：{student["score"]}')
            found = True
            break
    if not found:
            print("暂无该学生！")

def sort_students(students):
    students.sort(key=lambda student: student["score"], reverse=True)
    print("\n======学生成绩如下=======")
    show_students(students)



def judge_score(score):
    if 90 <= score <= 100:
        return "优秀"
    elif 80 <= score < 90:
        return "优良"
    elif 60 <= score < 80:
        return"及格"
    else:
        return"不及格"



while True:
    print("1，添加学生")
    print("2，列出所有学生成绩")
    print("3，计算全班平均分")
    print("4，查找特定学生成绩")
    print("5，删除特定学生成绩")
    print("6，修改特定学生的成绩")
    print("7，退出系统")

    try:
        choice = int(input("请输入号码："))
        if choice == 1:
            add_student(students)
            save_student(students)
        elif choice == 2:
            sort_students(students)
        elif choice == 3:
            average_score(students)
        elif choice == 4:
            find_student(students)
        elif choice == 5:
            delete_student(students)
            save_student(students)
        elif choice == 6:
            update_student(students)
            save_student(students)
        elif choice == 7:
            print("成功退出系统！")
            save_student(students)
            break
    except ValueError:
        print("请输入正确数字！")
