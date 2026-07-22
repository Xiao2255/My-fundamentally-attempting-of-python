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

