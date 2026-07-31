import random
import json
def save_game_record(records):
    with open("game_record.json", "w", encoding="utf-8") as f:
        json.dump(
            records,
            f,
            ensure_ascii=False,
            indent=4,
        )
#2026.7.31,新增了用户对局记录保存，优化了菜单选项管理
def load_game_record():
    try:
        with open("game_record.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_game_record():
    with open("game_record.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)


def simple_rock_paper_scissors():
    records = load_game_record()

    user_score = 100
    computer_score = 100
    round_count = 0
    print("剪刀石头布游戏开始！")
    print("输入说明：1=剪刀, 2=石头, 3=布")
    while 0 < user_score < 200:
        round_count += 1
        print(f"\n第{round_count}轮 - 用户:{user_score} 电脑:{computer_score}")
        user_input = (input("请出拳(1/2/3)，输入q退出: "))
        if user_input == "q":
                print("游戏结束！")
                break
        try:
            user = int(user_input)
            if user not in [1, 2, 3]:
                print("请输入1、2或3！")
                continue
        except ValueError:
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
    records.append({"user_score": user_score,
                    "computer_score": computer_score})
    save_game_record(records)
    print(f"\n游戏结束！最终分数 - 用户:{user_score}, 电脑:{computer_score}")
    if user_score >= 200:
        print("恭喜你赢了！")
    else:
        print("很遗憾你输了。")

if __name__ == "__main__":
    while True:
        print("A：再来一把")
        print("B:查看历史战绩")
        print("C:退出游戏")

        choice = input("请输入选项：").upper()
        if choice == "A":
            simple_rock_paper_scissors()
        elif choice == "B":
            read_game_record()
        elif choice == "C":
            print("退出游戏成功！")
            break
        else:
            print("请输入正确选项！")
