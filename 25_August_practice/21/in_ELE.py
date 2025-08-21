import random
import os
import time
from model import TITle, VOICE, RSP, GUIDELINE
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

def E_choice():
    e_choice =

def my_turn(top_floor):
    print(GUIDELINE[1])
    print(f"\n당신이 타고 있는 건물의 최고층은 \033[92m\033[40m{top_floor}층\033[0m이다.")
    time.sleep(2)
    present_floor = 1
    while present_floor != top_floor:
        print(f"\033[92m\033[40m{present_floor}F\033[0m")
        MIRROR()




















