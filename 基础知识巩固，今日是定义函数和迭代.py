def user(name, score):
    print(f"{name} 的成绩: {'及格' if score >=60 else '不及格'}")

user('泰迪' ,90)
user('张三', 80)

def multip(num1, num2):
    return num1 * num2
print(multip(156,532))

mlp = [x*x for x in range(1,11) if x % 2 == 0]
print(mlp)

lest1 = [(u + 2,y + 2)for u in range(4) for y in range(7)]
print(lest1)

#生成器：
gen = (x*x for x in range(5,15))
print(gen)

def my_fundation():
    for i in range(10):
        yield i
print(my_fundation())

#7.22 bmi计算器

name = input("请输入您的姓名：")
height =float(input("请输入您的身高(m)："))
weight =float(input("请输入您的体重(kg)："))
def calculate_bmi(height,weight):

    bmi = weight / (height * height)
    return bmi
bmi = calculate_bmi(height,weight)

def judge_bmi(bmi):
    if bmi >= 25:
        return "臭胖子"
    elif bmi <17:
        return "死竹竿"
    else:
        return "请继续保持"

result = judge_bmi(bmi)

def show_result(name,bmi,result):
    print(f"亲爱的：{name}, 您的健康体重指数为： {bmi:.2f}，我们给您的评价是：{result}")
show_result(name,bmi,result)
