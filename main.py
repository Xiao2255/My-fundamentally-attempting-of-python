from manager import *
from database import *

students = load_student()

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