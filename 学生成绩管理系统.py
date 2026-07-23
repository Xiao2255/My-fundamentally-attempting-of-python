#2026.7.23，今日自己用python写的学生成绩管理系统项目
students = []
def add_student(students):
    name = input("请输入学生姓名：")
    score  = int(input("请输入学生成绩："))
    student = {"name":name, "score": score}
    students.append(student)
    print("添加成功")

def show_student(students):
    if len(students) == 0:
        print("暂无学生信息")
        return
    for student in students:

        print(f"{student['name']}的成绩如下：{student['score']}")

def find_student(students):
    name = input("请输入学生姓名：")

    found = False

    for student in students:
        if student["name"] == name:
         print(f'{name}您好')
         print(f'您的成绩为{student["score"]}')
         found = True
    if found == False:
        print("对不起，您的成绩暂未录入，请稍后再试")

def delete_student(students):
    name = input("请输入需要删除地学生的姓名：")
    found = False
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("该学生信息删除成功")
            found = True
            break
    if found == False:
        print("对不起，系统暂无该学生信息")

def update_student(students):
    name = input("请输入要修改学生成绩的姓名：")
    found = False
    for student in students:
        if student["name"] == name:
            new_score = int(input("输入新的成绩："))
            student["score"] = new_score
            print("修改成功！")
            found = True
            break
    if found == False:
       print("暂未查询到该学生信息，无法修改成绩")

def statistics_student(students):
    if len(students) == 0:
        print("暂无学生，无法统计所有成绩")
        return
    count = len(students)
    print(f'学生总人数为：{count}')
    total = 0
    max_score = students[0]["score"]
    min_score = students[0]["score"]
    for student in students:
        total += student["score"]
        if  student["score"] > max_score:
            max_score = student["score"]
        if student["score"] < min_score:
            min_score = student["score"]
    average = total / count
    print(f'学生中最高分为：{max_score}, 学生中最低分为{min_score}, 学生的平均分为：{average}')

while True:
    print("=======学生管理系统=======")
    print("1，添加学生成绩")
    print("2，查看学生成绩")
    print("3，查找学生成绩")
    print("4，删除学生成绩")
    print("5，修改学生成绩")
    print("6，统计学生成绩")
    print("7，退出")


    choice = input("请选择：")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_student(students)
    elif choice == "3":
        find_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        update_student(students)
    elif choice == "6":
        statistics_student(students)
    elif choice == "7":
        print("退出")
        break
    else:
        print("请输入正确序号！")