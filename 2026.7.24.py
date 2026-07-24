from operator import truediv

students = []

def add_student(students):
    name = input("请输入学生姓名：")
    score  = int(input("请输入该学生成绩："))


    if score > 100 or score < 0:
        print("请输入正确成绩！")
        return
    student = {
        "name": name,
        "score": score}
    students.append(student)
    print("添加成功！")

def show_student(students):
    if len(students) == 0:
        print("暂无学生成绩")
        return
    for student in students:
        result = judge_score(student["score"])
        print(f'{student["name"]}的成绩为：{student["score"]}, {result}')

def find_student(students):
    name =  input("查找学生的姓名：")
    found = False
    for student in students:
        if student["name"] == name:
            result = judge_score(student["score"])
            print(f'{student["name"]}的成绩是{student["score"]},{result}')
            found = True
    if found == False:
            print("对不起，暂时无法找到该学生！")
            return

def judge_score(score):

  for student in students:
    if 100 >= score >=90:
        return "优秀"
    elif 90 >= score >=80:
        return "优良"
    elif 80 >= score >=70:
        return "良好"
    elif 70 >= score >=60:
        return "及格"
    else:
        return "不及格"


def sort_students(students):

    students.sort(key=lambda student: student["score"], reverse=True)
    print("成绩从上往下依次为：")
    for student in students:
        print(f'{student["name"]}: {student["score"]}')


while True:
    print("=======学生成绩管理系统=======")
    print("1，增加学生成绩")
    print("2，列出所有学生成绩")
    print("3，查询特定学生成绩")
    print("4，学生成绩依次排序")
    print("5，退出系统")

    choice = input("请输入号码：")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_student(students)
    elif choice == "3":
        find_student(students)
    elif choice == "4":
        sort_students(students)
    elif choice == "5":
        print("成功退出系统")
        break
    else:
        print("请输入正确号码")