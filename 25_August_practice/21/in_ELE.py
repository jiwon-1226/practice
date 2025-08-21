import random
import os
import time

from model import TITle, VOICE, E_RSP, P_RSP, GUIDELINE, W_L
from pictures import MIRROR



def show_title():
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
    return

def E_choice(p_choice, p_time):
    r_choice = random.choice(W_L)
    #승률 조작
    if p_time < 3:
        print("win")
    else:
        print("lose")




def my_turn(top_floor):
    print(GUIDELINE[1])
    print(f"\n당신이 타고 있는 건물의 최고층은 \033[92m\033[40m{top_floor}층\033[0m이다.")
    time.sleep(2)
    present_floor = 1
    while present_floor != top_floor:
        print(f"\n\033[92m\033[40m{present_floor}F\033[0m")
        MIRROR("", "")
        start = time.time()
        choice = input("1. 바위  2. 가위  3. 보 \n 선택:")
        end = time.time()

        input_time = end - start
        print(input_time)
        E_choice(choice, input_time)




my_turn(3)

















