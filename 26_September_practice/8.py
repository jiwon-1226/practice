import random

QnA = {"비갑개의 기능은?" : "모세혈관이 많마 공기를 따뜻하고 습하게 함",
       "코 전정의 특징과 기능은?" : "빈 공간 피부와 털로 덮여있음 점액을 분비"}


class Study:
    def __init__(self, question, answer):
        self.question = random.choice(QnA.keys())
        self.answer = QnA.values(self.question)
    def test_Q(self):
        while True:
            num = 0
            num += 1
            print(f"{num}번 문제: {self.question}")