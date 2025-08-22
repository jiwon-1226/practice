import random
import os
import time


from model import GUIDELINE


def end_w3():
    time.sleep(2)
    print()
    print(GUIDELINE[33])
    time.sleep(5)
    print("\n당신은 10번의 지시를 따라야 한다.\n")
    time.sleep(2)
    print(GUIDELINE[10])
    time.sleep(5)
    print("\n다행히 간단한 지시이다.\n")
    time.sleep(1)
    choice = input("1. 계단을 찾아서 계단으로 내려간다. \n2. 엘리베이터를 탄다.\n선택 :")
    if choice == "1":
        print("당신은 비상구 표시가 빛나는 곳으로 간다.")
        time.sleep(1)
        print("\n.....\n")
        time.sleep(3)
        print("당신은 계단을 찾았다.")
        time.sleep(1)
        print("계단으로 1층까지 내려간다.\n")
        time.sleep(2)
        print("\n터벅터벅\n")
        time.sleep(2)
        print("\n터벅터벅\n")
        time.sleep(2)
        print("\n터벅터벅\n")
        time.sleep(2)
        print("\n터벅터벅\n")
        time.sleep(2)
        print("\n터벅터벅\n")
        print("1층에 도착했다.")

        time.sleep(3)

        for i in range(100, 4, -1):
            print(f"   \033[92m\033[40m  [{i}F]  \033[0m", end="")
            time.sleep(0.3)
            print(end="\r")

        print("당신은 당장 그 건물을 도망쳐 니온다.")
        print("\033[90m\033[3m킥킥...\033[0m", end="")
        time.sleep(2)
        print(end="\r")
        print("\033[90m\033[3m깔깔깔깔\033[0m", end="")
        time.sleep(2)
        print(end="\r")
        print(" \n어라? 방금 무슨 소리 안들렸나?")
        print("\033[1mQterw-D-718", end="")
        time.sleep(2)
        print("\033[91m [거울을 보지 마세요]\033[0m")
        time.sleep(3)
        print("\n")


def do_not_direction():
    print("당신은 텍스트의 지시사항을 따르지 않았다.")
    print("거울 속 존재가 웃는다.")
    print("당신은 이제 집으로 돌아 갈 수 없다.")
    print("행운을 빈다")


end_w3()