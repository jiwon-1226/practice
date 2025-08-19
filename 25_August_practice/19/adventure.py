#모험 게임
import time
import os
from package.utils import load_player

#
# def manu():
#     if os.path.exists("save.json"):
#         while True:
#             fir_choice = input("1. 기존 게임 계속 진행하기\n2. 새로 시작하기")
#             if fir_choice == "1":
#                 player = load_player()
#                 sec_choice = input("1. 게임 계속 진행하기\n2. 종료하기\n선택:")
#                 if sec_choice == "1":
#                     print(f"{name}님의 레벨에 맞는 게임으로 이동합니다\n==========로딩중============")
#                     time.sleep(2)
#                     Game(name, level)
#                 elif sec_choice == "2":
#                     print("게임을 종료합니다")
#                     break
#                 else:
#                     print("잘못된 입력입니다")
#                     continue
#             elif fir_choice == "2":




class Talk:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        print(f"안녕하세요 {self.name}님!\n현재 {self.name}님의 레벨은 Lv.{self.level}입니다.")

class Game:
    def __init__(self, name, level):
        self.name = name
        self.name = level
    def answer(self):
        p_answer = input("답:")



class Level1(Game):
    def __init__(self, problem):
        self.problem = problem
    def level1_pro(self):
        #문제 호출

