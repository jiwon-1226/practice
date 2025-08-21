#mini game
#hangman - 괴담출근 버전

import random
import time
import os
from files import HANGMANGIVEN, HANGMANPICS, words
# from hang_game import my_game

words = ["consequential", "resume", "conduct", "qualification", "essential"]
players = ["은하제", "김솔음", "박민성", "서팔광", "엄석용", "박남살", "태백홍"]


print("===========로딩중==============")
time.sleep(2)
print()
print("괴담에 성공적으로 진입하였습니다.")
time.sleep(1.5)
print("\033[1mQterw-B-191", end="")
time.sleep(2)
print("\033[91m Hungry Hangman\033[0m")
time.sleep(2)
print("괴담은 항상 새 \033[1m선생님\033[0m을 반깁니다.")
time.sleep(1)
print("괴담이 선생님에 대해 알고싶어합니다.")
time.sleep(1)
name = input("\n선생님의 이름을 적어주세요\n이름:")
if name == "이름":
    time.sleep(2)
    print("\n\033[91m\033[3m이름?")
    time.sleep(2)
    print("\n\n'이름name,mymaster@'��(��) ���� �Ǵ� �ܺ� ���, ������ �� �ִ� ���α׷�, "
          "\n�Ǵ���ġ ������ �ƴմϴ�, ������ �� �ִ� ���α׷�, �Ǵ���ġ ������ �ƴմϴ�, "
          "\n��(��) ���� �Ǵ� �ܺ� ���, "
          "\n������ ��, ������ �� �ִ� ���α׷�.")
    time.sleep(1)
    print("\n\033[91m\033[3m이름님!!!!!!!\n\n")
    time.sleep(2)
    print("이름님을 믿니이이??")
    time.sleep(3)
    print(" ...None")
    time.sleep(0.5)
    print("\n\n이름님을 믿니?")
    time.sleep(2)
    print(" ..None")
    time.sleep(0.3)
    print("\n이름님을 믿니??\n")
    time.sleep(1)
    print(" None\n이름님을 믿니???\n")
    time.sleep(2)
    print(" None\n이름님을 믿니이???\n")
    time.sleep(2)
    print(" None\n이름님을 믿니이이이?????\n\n")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(3)
    print("\n이름님을 믿냐구우우우우우우??????????\n\033[0m")
    time.sleep(3)
    print("\033[31m\033[1m이런 무뢰배들 같으니라고....!!!!\033[0m", end="")
    time.sleep(4)
    print(end="\r")
    print("\033[37m이런, 실수했군요\033[0m", end="")
    time.sleep(3)
    print(end="\r")
    print("부속 유치원의 선생님은 저런 말을 쓰지 않아요 :)", end="")
    time.sleep(2)
    print(end="\r")
    print("기억하세요, 선생님은", end="")
    time.sleep(2)
    print("\033[91m\033[103m\033[1m 예쁘고 착한 말만 사용한답니다\033[0m\n\n")
    time.sleep(2)
    print("==================================")
    time.sleep(2)

players.append(name)
print(f"\033[32m{name}\033[0m선생님 반갑습니다! \n아이들이 오기 전에 행맨 게임을 하도록 합시다!")
time.sleep(1)
print()
print("=====괴담이 행맨을 고르는 중입니다=====")
print()
time.sleep(3)
#
# def conta():
#     global contamination
#     contamination = 0


blank_answer = []
answer = []
player_guess_list = []

def my_game(hangman, is_player=True):
    over = 0
    time.sleep(2)
    print("\n======단어를 선택하고 있습니다=======\n")
    time.sleep(3)
    word = random.choice(words)
    blank_count = len(word)
    print(f"{blank_count}개의 단어입니다")

    for j in range(0, len(word)):
        blank_answer.append("_")
    for i in word:
        answer.append(i)
    print(answer)


    while over != 1:
        hangman_life = 7
        while True:
            print(HANGMANPICS[7 - hangman_life])
            if len(player_guess_list) == 0:
                pass
            else:
                print(f"Inferred Letter: {", ".join(player_guess_list)}")
                print(' '.join(blank_answer))
            while True:
                player_guess = input("Input letter > ").lower()
                if not player_guess.isalpha():
                    print("please write alphabet :)", end="")
                    time.sleep(3)
                    print(end="\r")
                    continue
                if len(player_guess) >= 2:
                    print("write just one letter")
                    time.sleep(3)
                    print(end="\r")
                    continue
                else:
                    break
            player_guess_list.append(player_guess)


            # 사용자가 유추한 글다 중 하나가 선택된 단어 안에 있으면 출력
            if player_guess in answer:
                print("맞았습니다!")
                num = 0
                for m in word:
                    if player_guess == m:
                        blank_answer[num] = m
                    num += 1
                print(blank_answer)
            else:
                print("틀렸습니다")
                hangman_life -= 1
                print(f"{hangman}의 {HANGMANGIVEN[7 - hangman_life]}가 쟁반에 올라갑니다")
            os.system("cls")

            if answer == blank_answer:
                print(f"맞췄습니다! 정답은 {word}!")
                os._exit(os.EX_OK)

            elif hangman_life == 0:
                print(HANGMANPICS[6])
                print(f"정답은 {word}! 아쉽지만 {hangman}은 사망하였습니다. \n{hangman}의 시체는 괴담에 귀속됩니다.")
                os._exit(os.EX_OK)






def game_over():
    print("재밌는 시간이었습니다. 다음에 또 봅시다 선생님")
    os._exit(os.EX_OK)


hangman = random.choice(players)
print(f"행맨은 \033[34m{hangman}\033[0m입니다!")
players.remove(hangman)


if hangman == name:
    print("당신의 목에 절취선이 그어졌습니다.")
    time.sleep(1.5)
    print("당신의 동료들이 \033[4m단어를 다 맞춘다면\033[0m", end="")
    time.sleep(1.5)
    print("\033[91m\033[1m 당신은 죽습니다\033[0m")
    time.sleep(2)
    print("\033[91m\033[3m그렇다고 동료들이 단어를 안맞춘다고 해서 당신이 안죽는 건 아닙니다\033[0m")
    time.sleep(1)
    print("\033[91m킥")
    time.sleep(0.5)
    print("\033[3m킥\033[4m킥\033[0m")
    time.sleep(1.5)
    print("(괴담이 당신을 비웃습니다)")
    time.sleep(1.5)
    print("\033[91m\033[3m부디 행운을 빕니다, 행맨.\033[0m")
    my_game(hangman, False)
else:
    time.sleep(0.5)
    print(f"(\033[34m{hangman}\033[0m의 목에 절취선이 그어집니다)")
    time.sleep(1)
    print(f"\033[34m{hangman}\033[0m : 컥! 커억...!")
    print()
    print("선생님들은 행맨을 위해 박수쳐주세요!")
    your_choice = input("1. 박수를 친다\n2. 괴담을 향해 욕을 한다\n3. 행맨을 조롱한다\n4. 아무것도 하지 않는다\n 숫자를 입력해주세요:")
    if your_choice == "1":
        print("\033[3m짝짝짝짝\033[0m")
        time.sleep(1.5)
        print("(당신의 순종적인 행동에 괴담이 좋아합니다)")
        time.sleep(1.5)
        print("다들 착한 선생님입니다.")
        my_game(hangman, True)
    else:
        print("유치원에 정적이 흐릅니다")
        time.sleep(3)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(1)
        print("교육서를 따르지 않는 선생님에게는 교육이 필요합니다")
        time.sleep(1)
        print("(괴담이 당신에게 교육서를 줍니다)")
        time.sleep(1)
        print("(손이 저절로 펴져서 교육서를 읽기 시작합니다)")
        time.sleep(1)
        time.sleep(5)
        print("====오염 진행 20%======")
        my_game(True)





