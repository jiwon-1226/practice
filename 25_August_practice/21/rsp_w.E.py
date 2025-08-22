import random
import os
import time

from model import HOW_ENTER, BUTTON, PRESS_BUTTON, VOICE, GUIDELINE, top_floor_list
from in_ELE import show_title, my_turn
from pictures import REPAIR, ELEVATOR

#괴담 입장 방법
def enter_gs():
    print("==========================")
    print("         loding...        ", end="")
    time.sleep(3)
    e = random.choice(HOW_ENTER)
    print(end="\r")
    time.sleep(1)
    print(e)
    time.sleep(1)
    e_choice = input("\n1. 한다 \n2. 안한다\n선택:")
    top_floor = random.choice(top_floor_list)
    if e_choice == "1":
        time.sleep(1)
        print("당신은 그 괴담이 잘 나타난다고 소문이 난 아파트를 찾아간다.\n")
        time.sleep(2)
        print(ELEVATOR("close_repair", 2),
              "엘리베이터가 한대 뿐인 건물에서 주로 발생하며 \n"
              "특히 잔고장이 잦거나 수리 중이라는 종이가 붙은 엘리베이터를 타야 괴담에 진입할 확률이 높다고 한다.\n")
        time.sleep(3)
        print(REPAIR[0],
              "역시나 엘리베이터에 수리 중이라는 종이가 붙어있다.\n")
        time.sleep(2)
        print("당신은 버튼을 누르고 탑승한다.\n")
        BUTTON("^")
        time.sleep(1.5)
        print(end="\r")
        PRESS_BUTTON("^")
        time.sleep(2)
        print(end="\r")
        BUTTON("^")
        time.sleep(1)
        print("\n")
        VOICE("close")

        print("\n엘리베이터에 탑승한 당신은 아무버튼도 누르지 않았지만 엘리베이터가 움직인다.")
        time.sleep(1)
        show_title(top_floor)
        time.sleep(2)
        print("당신은 텍스트 파일에서 읽었던 첫번째 문장을 다시 꺼내어 본다.")
        print(GUIDELINE["f"])
        print("\n당신은 기대하며 거울 속의 자신을 바라본다.\n")
        my_turn(top_floor)

    elif e_choice == "2":
        time.sleep(1)
        print("당신은 텍스트 파일을 대충 훑어보고 잊는다")
        time.sleep(2)
        print("귀가 중인 당신.\n당신의 아파트 엘리베이터에 탑승한다.\n"
              "이상하게 느낌이 좋지 않았다")
        time.sleep(1)
        print("..불안한 마음을 달래기 위해 휴대폰을 연신 들여다 본다.")
        VOICE("close")
        time.sleep(2)
        print("....어라?")
        time.sleep(2)
        print("\033[31m당신이 엘리베이터 버튼을 누른적이 있던가?\033[0m\n")
        time.sleep(2)

        show_title(top_floor)

        time.sleep(2)
        print("당신은 텍스트 파일에서 읽었던 첫번째 문장을 다시 꺼내어 본다.")
        print(GUIDELINE["f"])
        time.sleep(1)
        print("뭐 대충 이런 내용이었던거 같다.")
        time.sleep(1)
        print("\n당신의 등에서 식은땀이 흐른다.")
        print("당신은 텍스트 파일을 연 휴대폰을 꾹 쥐고 지시사항을 따른다.")
        my_turn(top_floor)


    else:
        print("당신은 뭐 이런걸 믿겠냐고 코웃음을 친다")
        time.sleep(1)
        print("\033[90m\033[3m킥킥\033[0m", end="")
        time.sleep(2)
        print(end="\r")
        print(" \n어라? 방금 무슨 소리 안들렸나?")
        time.sleep(1)
        print("....모르겠다!")
        print("당신은 친구와의 약속장소로 향한다.")
        time.sleep(1)
        print("\n...\n")
        time.sleep(1)
        print("약속장소에 먼저 도착한 당신은 친구에게 먼저 들어가 있겠다는 말을 남기고\n엘리베이터에 탑승한다.")
        ELEVATOR("close_repair", 1)
        time.sleep(1)
        ELEVATOR("opening", 1)
        time.sleep(1)
        ELEVATOR("open", 1)

        my_turn(top_floor)

        print("여기로 옴!")






enter_gs()