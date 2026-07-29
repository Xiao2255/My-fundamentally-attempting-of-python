import json

#2026.7.29，新增保存json项目，将数据全部保存进json中
def save_students(students):
    data = []

    for student in students:
        data.append({
            "name": student.name,
            "score": student.score
        })

    with open("students.json", "w", encoding = "utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
        )

#2026.7.29，将add_student等全部从字典（dict）改成了对象
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def show(self):
        print(f'姓名：{self.name}, 成绩：{self.score}, 等级：{self.get_grade()}')

    def get_grade(self):

        if 100 >= self.score >= 90:
            return "优秀"
        elif 90 >= self.score >= 80:
            return "优良"
        elif 80 >= self.score >= 70:
            return "良好"
        elif 70 >= self.score >= 60:
            return "及格"
        else:
            return "不及格"

def load_student():
    try:
        with open("students.json", "r",encoding="utf-8") as f:
            data = json.load(f)
        students = []

        for item in data:
            student = Student(item["name"],item["score"])
            students.append(student)

        return students
    except:
        return []

students = load_student()

def add_student(students):
   name = input("请输入学生姓名：")


   for student in students:
            if student.name == name:
                print("该学生已存在！无法添加！")
                return

   while True:
      try:

         score = int(input("请输入该学生成绩："))
         if 0<= score <= 100:
             break
         else:
            print("请输入正确分数！（0———100）")
      except ValueError:
         print("请输入数字！")

   student = Student(name,score)
   students.append(student)
   print("添加成功！")

def show_student(students):
    if len(students) == 0:
        print("暂无学生成绩")
        return
    for student in students:
        student.show()

def find_student(students):
    name =  input("查找学生的姓名：")
    found = False
    for student in students:
        if student.name == name:
            print(f'{student.name}的成绩是{student.score},等级为：{student.get_grade()}')
            found = True
    if found == False:
            print("对不起，暂时无法找到该学生！")
            return
#2026.7.29日删改内容：（判断了更新后成绩的合理性)
def alter_student(students):
    name = input("请输入需要修改学生的姓名：")
    found = False
    for student in students:
        if student.name == name:

            while True:
               try:
                   score = int(input("请输入更新后的成绩："))
                   if 0 <= score <= 100:
                          break
                   else:
                       print("请输入正确成绩！")
               except ValueError:
                   print("请输入数字！")

            student.score = score
            print(f'修改成功！当前{student.name}的成绩更新后为{student.score}')
            found = True
            break
    if found == False:
        print("暂无该学生信息！")
#2026.7.27日新增内容：
def delete_student(students):
    name = input("请输入被删除学生的姓名：")
    found = False
    for student in students:
        if student.name == name:
            students.remove(student)
            print("删除成功！")
            found = True
            break
    if found ==False:
            print("暂无该学生信息！")
            return

def sort_students(students):

    students.sort(key=lambda student: student.score, reverse=True)

def average_score(students):
    if len(students) == 0:
        print("暂无学生成绩！")
        return
    count = len(students)
    print(f'学生的人数为{count}')
    max_score = students[0].score
    min_score = students[0].score
    for student in students:
        if student.score < min_score:
            min_score = student.score
        if student.score > max_score:
            max_score = student.score
    total = 0
    for student in students:
        total += student.score
    average = round(total / len(students),2)
    print(f'学生中最高分为{max_score},最低分为：{min_score},全部学生的平均分为：{average}')



while True:
    print("=======学生成绩管理系统=======")
    print("1，增加学生成绩")
    print("2，列出所有学生成绩")
    print("3，查询特定学生成绩")
    print("4，学生成绩依次排序")
    print("5，删除特定学生成绩")
    print("6，修改特定学生及成绩")
    print("7，计算全学生人数和平均分")
    print("8，退出系统")

    choice = input("请输入号码：")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_student(students)
    elif choice == "3":
        find_student(students)
    elif choice == "4":
        sort_students(students)
        show_student(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        alter_student(students)
    elif choice == "7":
        average_score(students)
    elif choice == "8":
        save_students(students)
        print("保存成功，退出系统成功！")
        break
    else:
        print("请输入正确号码！")