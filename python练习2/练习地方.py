#读取不存在文件练习
try:
    with open("student.txt", "r", encoding="utf-8")as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("该文件不存在！")


text = input("请输入需要保存的内容：")
with open("node.txt", "w", encoding="utf-8") as f:
        f.write(text)
        print("保存成功！")

with open("node.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print("保存的内容如下：")
        print(data)




























#中断练习
while True:
    try:
        age = int(input("请输入年龄：" ))
        break
    except ValueError:
        print("请输入数字！")





