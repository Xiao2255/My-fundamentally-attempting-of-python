import random
def simple_rock_paper_scissors():
    user_score = 100
    computer_score = 100
    round_count = 0
    print("剪刀石头布游戏开始！")
    print("输入说明：1=剪刀, 2=石头, 3=布")
    while 0 < user_score < 200:
        round_count += 1
        print(f"\n第{round_count}轮 - 用户:{user_score} 电脑:{computer_score}")
        try:
            user = int(input("请出拳(1/2/3): "))
            if user not in [1, 2, 3]:
                print("请输入1、2或3！")
                continue
        except:
            print("输入无效！")
            continue
        computer = random.randint(1, 3)
        choices = ["剪刀", "石头", "布"]
        print(f"你: {choices[user - 1]}, 电脑: {choices[computer - 1]}")
        if user == computer:
            print("平局！")
        elif (user == 1 and computer == 3) or \
                (user == 2 and computer == 1) or \
                (user == 3 and computer == 2):
            print("你赢了！+10分")
            user_score += 10
            computer_score -= 10
        else:
            print("你输了！-10分")
            user_score -= 10
            computer_score += 10
    print(f"\n游戏结束！最终分数 - 用户:{user_score}, 电脑:{computer_score}")
    if user_score >= 200:
        print("恭喜你赢了！")
    else:
        print("很遗憾你输了。")
if __name__ == "__main__":
    simple_rock_paper_scissors()