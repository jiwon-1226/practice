#mini game
#hangman - 괴담출근 버전

import random
import time

words = ["consequential", "resume", "conduct", "qualification", "essential"]
players = ["은하제", "김솔음", "박민성", "서팔광", "엄석용", "박남살", "태백홍"]



print("===========로딩중==============")
time.sleep(2)
print("괴담에 성공적으로 진입하였습니다.\n괴담은 항상 새 선생님을 반깁니다.")
time.sleep(1.5)
name = input("선생님의 이름을 적어주세요\n이름:")
players.append(name)
print(f"{name}선생님 반갑습니다! \n아이들이 오기 전에 행맨 게임을 하도록 합시다!")
time.sleep(1)
print("=====괴담이 행맨을 고르는 중입니다=====")
time.sleep(3)
#
# def conta():
#     global contamination
#     contamination = 0



def my_game(is_player=True):
    time.sleep(2)
    print("======단어를 선택하고 있습니다=======")
    time.sleep(3)
    word = random.choice(words)
    blank_count = len(word)
    print(f"{blank_count}개의 단어입니다")
    print("_" * blank_count)
    print(word)
    time.sleep(1)
    print("단어를 맞춰봅시다")
    while is_player:
        my_a = input("단어를 작성해주세요 : ")
        if my_a in word is True:
            print("와! 맞아요!")



hangman = random.choice(players)
print(f"행맨은 {hangman}입니다!")
players.remove(hangman)


if hangman == name:
    print("당신의 목에 절취선이 그어졌습니다.")
    time.sleep(1.5)
    print("당신의 동료들이 단어를 다 맞춘다면 당신은 죽습니다")
    time.sleep(1.5)
    print("그렇다고 동료들이 단어를 안맞춘다고 해서 당신이 안죽는 건 아닙니다")
    time.sleep(1)
    print("킥")
    time.sleep(0.5)
    print("킥킥")
    time.sleep(1.5)
    print("(괴담이 당신을 비웃습니다)")
    time.sleep(1.5)
    print("부디 행운을 빕니다, 행맨.")
    my_game(False)
else:
    time.sleep(0.5)
    print("선생님들은 행맨을 위해 박수쳐주세요!")
    your_choice = input("1. 박수를 친다\n2. 괴담을 향해 욕을 한다\n3. 행맨을 조롱한다\n4. 아무것도 하지 않는다\n 숫자를 입력해주세요:")
    if your_choice == "1":
        print("짝짝짝짝")
        time.sleep(1.5)
        print("(당신의 순종적인 행동에 괴담이 좋아합니다)")
        time.sleep(1.5)
        print("다들 착한 선생님입니다.")
        my_game(True)
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
        contamination += 20
        time.sleep(5)
        print("====오염 진행 20%======")
        my_game(True)





