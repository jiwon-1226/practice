import random
import os
import time

from fontTools.misc.cython import returns

from model import TITle, VOICE, E_RSP, P_RSP, GUIDELINE, ALLBUTTON, fast_p_win, slow_p_lose
from pictures import MIRROR, GLASS



def show_title(top_floor):
    print("괴담에 성공적으로 진입하였다.")
    time.sleep(1.5)
    print("\033[1mQterw-D-718", end="")
    time.sleep(2)
    print("\033[91m [거울을 보지 마세요]\033[0m\n")
    time.sleep(3)
    for i in TITle:
        print(i)
        time.sleep(0.5)
    time.sleep(2)

    VOICE("go_up")
    time.sleep(1)
    ALLBUTTON(top_floor)
    time.sleep(1)
    print("\n모든 층의 버튼이 눌려져 있다.\n")
    time.sleep(2)
    print("....물론 당신은 누른 적이 없다.\n")

    return



def E_choice(p_choice, input_time):
    #승률 조작
    if input_time < 1.5:
        r_choice = random.choice(fast_p_win)
    else:
        r_choice = random.choice(slow_p_lose)
    if r_choice == "lose":
        if p_choice == "1":
            MIRROR("3", "")
            print("you lose")
            return -1

        elif p_choice == "3":
            MIRROR("3", "")
            print("Tie, Draw")
            return 0

        else:
            MIRROR("1", "")
            print("you lose")
            return -1

    elif r_choice == "win":
        if p_choice == "1":
            MIRROR("1", "")
            print("Tie, Draw")
            return 0

        elif p_choice == "3":
            MIRROR("1", "")
            print("you win")
            return 1
        elif p_choice == "2":
            MIRROR("3", "")
            print("you win")
            return 1
        else:
            MIRROR("3", "")
            print("Tie, Draw")
            return 0

    else:
        MIRROR(p_choice, "")
        print("Tie, Draw")
        return 0







def my_turn(top_floor):
    lose_count = 0
    win_count = 0

    print(GUIDELINE[1])
    print(f"\n당신이 타고 있는 건물의 최고층은 \033[92m\033[40m{top_floor}층\033[0m이다.")
    time.sleep(2)
    present_floor = 1

    while True:
        if present_floor <= top_floor:
            print(f"\n\033[92m\033[40m{present_floor}F\033[0m")
            MIRROR("", "")
            time.sleep(2)
            start = time.time()
            p_choice = input("1. 바위  2. 가위  3. 보 \n 선택:")
            end = time.time()
            input_time = end - start

            result = E_choice(p_choice, input_time)

            if result == 1:
                win_count += 1
                print(win_count)
            elif result == -1:
                lose_count += 1
            else:
                win_count += 0
            print(f"이김 : {win_count}, 짐 : {lose_count}")
            present_floor += 1


        elif present_floor > top_floor:
            print(f"이긴 횟수: {win_count}")

            if win_count != 0:
                time.sleep(1)
                print("당신은 최고층에 도착했다.")
                time.sleep(1)
                print(GUIDELINE[1])
                time.sleep(3)
                print(f"\n당신이 '거울 속 존재'를 이긴 횟수는 {win_count}, \n다행히 0번이 아니다.")
                time.sleep(2)
                print(GUIDELINE[3])
                time.sleep(2)
                print("\033[90m\033[3m쳇, 운이 좋군...\033[0m", end="")
                time.sleep(2)
                print(end="\r")
                print("    ")
                time.sleep(1)
                print(".....?", end="")
                time.sleep(2)
                print(end="\r")
                print("당신은 기뻐하며 3번 지시문을 마저 읽는다.")
                print("\n", GUIDELINE[3-2])
                print(f"당신은 {top_floor}에 내려서 유리창을 찾는다.")

                Answer_Q()

            else:
                break


def Answer_Q():
    print("\n ......")
    time.sleep(3)
    print("\n찾았다!")
    time.sleep(1)
    GLASS("just")




my_turn(4)











