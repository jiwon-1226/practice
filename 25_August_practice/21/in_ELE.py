import random
import os
import time
from pdb import line_prefix

from model import TITle, VOICE, GUIDELINE, ALLBUTTON, ffast_p_win, fslow_p_lose, sfast_p_win, sslow_p_lose,  gA
from pictures import MIRROR, ELEVATOR
from end import end_wr3, end_w99, end_ww3, GLASS



def show_title(top_floor):
    print("괴담에 성공적으로 진입하였다.\n\n\n\n\n\n")
    time.sleep(3)
    print("\033[1mQterw-D-718", end="")
    time.sleep(2)
    print("\033[91m [거울을 보지 마세요]\033[0m")
    time.sleep(3)
    print("\n")
    for t in TITle:
        print(t)
    print("\n\n\n\n\n\n")
    time.sleep(7)

    VOICE("go_up", top_floor)
    time.sleep(1)
    ALLBUTTON(top_floor)
    time.sleep(1)
    print("\n모든 층의 버튼이 눌려져 있다.\n")
    time.sleep(2)
    print("....물론 당신은 누른 적이 없다.\n")

    return



def E_choice(p_choice, input_time, fast_p_win, slow_p_lose):
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
    time.sleep(1)
    print(f"\n당신이 타고 있는 건물의 최고층은 \033[92m\033[40m{top_floor}층\033[0m이다.")
    time.sleep(2)
    present_floor = 1

    while True:
        if present_floor <= top_floor:
            print(f"\n\033[92m\033[40m[{present_floor}F]\033[0m")
            MIRROR("", "")
            time.sleep(2)
            start = time.time()
            p_choice = input("1. 바위  2. 가위  3. 보 \n 선택:")
            end = time.time()
            input_time = end - start

            result = E_choice(p_choice, input_time, ffast_p_win, fslow_p_lose)

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
                time.sleep(1)
                print("\n ......")
                time.sleep(3)
                print("\n찾았다!")
                time.sleep(1)
                GLASS(top_floor)
                end_wr3(top_floor)
                return

            else:
                print("당신은 모든 가위바위보를 졌다.")
                other_turn(top_floor)
                return

def other_turn(top_floor):
    print("\n")
    print(GUIDELINE[13])
    time.sleep(4)
    print(f"{top_floor}층에 도달할 때까지 한 번도 이기지 못한 당신을 거울 속에 당신이 활짝 웃으며 바라본다.")
    time.sleep(2)
    print(MIRROR("", "좋음"))
    time.sleep(2)
    print("\n모든 버튼의 불이 다 꺼졌다.\n\n")
    time.sleep(2)
    print(MIRROR("", "좋음", 0))
    time.sleep(2)
    print("거울 속의 엘리베이터 문은 활짝 열려있다.")
    time.sleep(2)
    print("    \033[92m\033[40m  [1930819F]  \033[0m")
    print("\n")
    print(GUIDELINE[132])
    print("\n")
    time.sleep(5)
    print("당신은 6번 지시사항으로 넘어간다.")
    time.sleep(2)
    print(GUIDELINE[6])
    time.sleep(3)
    print("\n")
    print(GUIDELINE[62])
    time.sleep(5)

    lose_count = 0
    win_count = 0

    time.sleep(2)
    game_count = 1

    while True:
        print("    \033[92m\033[40m  [1930819F]  \033[0m")
        MIRROR("", "웃음")
        print(f"{game_count}번째")
        time.sleep(2)
        start = time.time()
        p_choice = input("1. 바위  2. 가위  3. 보 \n 선택:")
        end = time.time()
        input_time = end - start

        result = E_choice(p_choice, input_time, sfast_p_win, sslow_p_lose)

        if result == 1:
            win_count += 1
            print("드디어 당신이 이겼습니다")
            MIRROR("", "매우나쁨")
            time.sleep(2)
            end_ww3(top_floor, lose_count)
            return

        elif result == -1:
            lose_count += 1
            MIRROR("", "매우좋음")
            time.sleep(2)
            print("\n'거울 속의 존재'가 당신의 패배를 기뻐합니다.\n")
            print(GUIDELINE[63])
            print("'거울 속의 존재'는 손가락을 움직여 거울에 자국을 남긴다")
            print("\n\n|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  f"|\033[47m\033[3m     {gA[lose_count -1]}                     \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n")
            time.sleep(3)
            Q = input("답:")
            Q_count = int(len(Q))
            space1 = 25 - Q_count
            time.sleep(3)
            print("\n\n|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  f"|\033[47m\033[3m     {gA[lose_count -1]}                     \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  f"|\033[47m    \033[1m\033[30m{Q[:20]}", end="")
            print(" " * space1, "\033[0m|")
            print("|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n"
                  "|\033[47m                                    \033[0m|\n")


            if lose_count == 3:
                print("\033[3m\033[37m킥", end="")
                time.sleep(2)
                print(end="\r")
                print("키킥, ", end="")
                time.sleep(2)
                print("키키킥\033[0m", end="")
                time.sleep(2)
                print(end="\r")
                end_w99()
                return



        else:
            win_count += 0
        print(f"이김 : {win_count}, 짐 : {lose_count}")
        game_count += 1










