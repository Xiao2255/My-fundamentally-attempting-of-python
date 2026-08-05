class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def show(self):
        print(f'\n{self.name}的成绩为{self.score}，等级为：{self.judge_score()}')

    def judge_score(self):
        if 90 <= self.score <= 100:
            return "优秀"
        elif 80 <= self.score < 90:
            return "优良"
        elif 60 <= self.score < 80:
            return "及格"
        else:
            return "不及格"