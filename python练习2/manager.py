from decorators import log_operation
from student import Student

@log_operation
def add_student(students):
    name = input("请输入学生姓名：")
    for student in students:
        if student.name == name:
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
    student =Student(name,score)
    students.append(student)

def average_score(students):
    if len(students) == 0:
        print("暂无学生！")
        return
    total = 0
    for student in students:
        total += student.score
    avg = round(total / len(students), 2)
    max_score = students[0].score
    min_score = students[0].score
    max_student = students[0].name
    min_student = students[0].name
    for student in students[1:]:
            if student.score > max_score:
                max_student = student.name
                max_score = student.score
            if  student.score < min_score:
                min_student = student.name
                min_score = student.score
    print(f'全班的平均分为：{avg}，其中，全班最高分为：{max_student},是{max_score};最低分为：{min_student}, {min_score}')

def find_student(students):
    name = input("请输入需要查找学生的名字：")
    found = False
    for student in students:
        if name in student.name:
         print(f'{student.name}的成绩为：{student.score}')
         found = True
    if not found:
            print("暂无该学生信息！")

@log_operation
def delete_student(students):
    name = input("请输入需要删除学生的姓名：")
    found = False
    for student in students:
        if student.name == name:
            students.remove(student)
            print("删除成功！")
            found = True
            break
    if not found:
            print("暂无该学生信息！")

@log_operation
def update_student(students):
    name = input("请输入需要更新成绩的学生的姓名：")
    try:
        new_score = int(input("请输入更新后的成绩："))
        if new_score < 0 or new_score > 100:
            print("请输入正确数字！")
            return
    except ValueError:
        print("请输入数字！")
        return
    found = False
    for student in students:
        if student.name == name:
            student.score = new_score
            print(f'修改成功！{name}当前的新成绩为：{student.score}')
            found = True
            break
    if not found:
            print("暂无该学生！")

def sort_students(students):
    students.sort(key=lambda student: student.score, reverse=True)
    print("\n======学生成绩如下=======")
    for student in students:
        student.show()