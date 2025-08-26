import random
import os
import time


from model import GUIDELINE, VOICE, BUTTON, PRESS_BUTTON, ANSWER
from pictures import MIRROR, ELEVATOR


def Reply_Q(space1, space2, Q):

    print("\n\n||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          f"||\033[47m    \033[1m\033[30m{Q[:20]}", end="")
    print(" "*space1, "\033[0m||")
    print(f"||\033[47m    \033[1m\033[30m{Q[20:]}", end="")
    print(" "*space2, "\033[0m||")
    print("||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n")



def GLASS(top_floor):
    print("=====================================\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "||\033[47m                \033[0m|| )\033[47m             \033[0m||\n"
              "||\033[47m                \033[0m||_|\033[47m             \033[0m||\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "||\033[47m                \033[0m||\033[47m               \033[0m||\n"
              "=====================================")

    time.sleep(2)
    print("\n\n\n먼지가 쌓인 더러운 창문이 보인다. 손가락으로 글을 쓰면 써질 것 같다. \n\n\n")
    time.sleep(2)
    print("=================================================\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m|| )\033[47m                   \033[0m||\n"
          "||\033[47m                      \033[0m||_|\033[47m                   \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "||\033[47m                      \033[0m||\033[47m                     \033[0m||\n"
          "=================================================")

    time.sleep(2)

    print("\n\n||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m|| )\033[47m                \033[0m\n"
          "||\033[47m                          \033[0m||_|\033[47m                \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          "||\033[47m                          \033[0m||\033[47m                  \033[0m\n"
          )

    time.sleep(2)

    print("\n\n||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n"
          "||\033[47m                                    \033[0m||\n")

    while True:

        Q = input("질문:")
        Q_count = int(len(Q))


        if Q_count <= 20:
            space1 = 25 - Q_count
            space2 = 31
            Reply_Q(space1, space2, Q)
        elif 20 < Q_count <= 40:
            space1 = 11
            space2 = 25 - (Q_count-20)
            Reply_Q(space1, space2, Q)
        else:
            Q = "40자 이내로 쓰시오."
            print("\n\n||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  f"||\033[47m    \033[1m\033[30m{Q}               \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  "||\033[47m                                    \033[0m||\n"
                  )
            continue

        A = random.choice(ANSWER)
        A_count = int(len(A))

        print("\n.....")
        time.sleep(5)

        if A_count <= 20:
            space1 = 32 - A_count
            space2 = 31
            Reply_Q(space1, space2, A)

        time.sleep(2)
        to_do = input("1. 답변이 마음에 든다. \n2. 답변이 마음에 들지 않는다. \n선택 :")
        if to_do == "1":
            print("\n당신은 답변을 마음에 들어하며 유리창에서 멀어진다.")
            time.sleep(2)
            return

        elif to_do == "2":
            print("\n당신은 당신의 질문에 대한 답변이 마음에 들지 않는다.\n")
            time.sleep(2)
            print("\033[3m\033[91m그런데 어쩌라고?", end="")
            time.sleep(2)
            print(end="\r")
            print("답변이 마음에 안들면 질문을 잘했어야지\033[0m", end="")
            time.sleep(2)
            print(end="\r")
            print("아쉽지만 질문을 할 수 있는 기회는 단 한번이기에 \n 더 이상 질문할 수 없다:)")
            time.sleep(2)
            print("당신은 체념하며 유리창에서 멀어진다.")
            return

        else:
            print("당신은 터무니없는 답변에 분노한다.")
            angry = input("1. 옆에 있는 돌로 유리창을 깬다. \n2. 이름님을 믿냐고 묻는다. \n3. 화가나지만 어떻게 할 수 없으므로 포기한다.\n선택:")
            if angry == "3":
                time.sleep(2)
                print("당신은 체념하며 유리창에서 멀어진다.")
                return

            elif angry == "2":
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
                print(" ...")
                time.sleep(0.5)
                print("\n\n이름님을 믿니?")
                time.sleep(2)
                print(" ..")
                time.sleep(0.3)
                print("\n이름님을 믿니??\n")
                time.sleep(1)
                print(" .\n이름님을 믿니???\n")
                time.sleep(2)
                print(" .\n이름님을 믿니이???\n")
                time.sleep(2)
                print("  \n이름님을 믿니이이이?????\n\n")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(0.5)
                print(".")
                time.sleep(3)
                print("\n이름님을 믿냐구우우우우우우??????????\n\033[0m")
                time.sleep(3)
                print("\n\033[92m\033[1m이런 미친 사이비였군.\033[0m")
                time.sleep(4)
                print("\033[92m그럼 필요없지.\033[0m")
                time.sleep(2)
                print("\n\n당신의 몸이 멋대로 움직이며 엘리베이터에 탑승한다.\n\n")
                time.sleep(2)
                VOICE("go_down", top_floor)

                VOICE("open", 1)
                print("엘리베이터가 \033[92m\033[40m 1층 \033[0m에 도착했다.")
                print("당신의 몸이 멋대로 엘리베이터에서 나간다.")

                print("\n\033[92m[문이 닫힙니다.]\033[0m")
                time.sleep(1)
                ELEVATOR("open_out", 1)
                time.sleep(1)
                ELEVATOR("opening_out", 1)
                time.sleep(1)
                ELEVATOR("close_repair", 1)
                time.sleep(4)

                print("\n\n\033[90m\033[3m꺼져.\033[0m", end="")
                time.sleep(2)
                print(end="\r")
                print("\033[90m\033[3m다신 오지마. 더러운 사이비.\033[0m", end="")
                time.sleep(2)
                print(end="\r")
                print(" \n킥킥 이름님을 믿니??", end="")
                time.sleep(2)
                print(end="\r")
                print("어라? 내가 뭐라고 말했던거지?\n")
                time.sleep(2)
                print("\033[1mQterw-D-718", end="")
                time.sleep(2)
                print("\033[91m [거울을 보지 마세요]\033[0m")
                time.sleep(3)
                print("\n")



            else:
                time.sleep(2)
                print("쾅!!")
                time.sleep(2)
                print("\033[3m쨍\0330m\033[1m\033[37m그\0330m\033[1m\033[4m랑\033[0m")
                print("당신은 텍스트의 지시사항을 따르지 않았다.")
                end_w99()
                return
    return



def end_wr3(top_floor):
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
        print("1층에 도착했다.\n")
        time.sleep(3)
        print("당신은 무심코 엘리베이터 쪽을 쳐다본다.\n")
        time.sleep(2)
        print("   \033[92m\033[40m  [100F]  \033[0m", end="")
        time.sleep(3)

        for i in range(100, 3, -1):
            print(end="\r")
            print(f"   \033[92m\033[40m  [{i}F]  \033[0m", end="")
            time.sleep(0.05)

        print(end="\r")
        print("\n\n당신은 당장 그 건물을 도망쳐 니온다.\n\n")
        time.sleep(2)
        print("\033[90m\033[3m킥킥...\033[0m", end="")
        time.sleep(2)
        print(end="\r")
        print("\033[90m\033[3m깔깔깔깔\033[0m", end="")
        time.sleep(2)
        print(end="\r")
        print(" \n어라? 방금 무슨 소리 안들렸나?\n")
        time.sleep(2)
        print("\033[1mQterw-D-718", end="")
        time.sleep(2)
        print("\033[91m [거울을 보지 마세요]\033[0m")
        time.sleep(3)
        print("\n")
    elif choice == "2":
        print("")

def end_ww3(top_floor, lose_count):
    time.sleep(3)
    print("\033[1m\033[3m\033[37m쾅!!")
    time.sleep(2)
    print("쾅! 쾅!\033[0m")
    time.sleep(1)
    print("\n'거울 속 존재'가 거울에 머리를 처박는다.")
    time.sleep(2)
    print("＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n",
          "|                                       |\n",
          "|                                       |\n",
          "|         금이 간 거울              |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"
          )

    time.sleep(2)

    print("\n\033[1m\033[3m\033[37m쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\n\n"
          "쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\n\n"
          "쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\n\n"
          "쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\n\n"
          "쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\n\n"
          "쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!쾅!\033[0m\n")

    time.sleep(2)

    print("＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|      거의 다 깨진 거울                |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "|                                       |\n",
          "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"
          )

    time.sleep(2)
    print("\n거울에 금이가고 깨진다. 그러나 ")
    time.sleep(2)
    print("\033[91m\033[3m'나'는\033[0m", end="")
    time.sleep(2)
    print(end="\r")
    print("'거울 속 존재'는 ", end="")
    time.sleep(2)
    print("거울에서 나오지 못한다.\n")
    time.sleep(2)
    print("......")
    time.sleep(3)
    MIRROR("", "", "")
    time.sleep(2)
    MIRROR("", "매우나쁨", "")
    time.sleep(2)
    print("\n\033[91m\033[3m깔깔깔깔!!\033[0m\n")
    time.sleep(3)
    print("거울 속에 열린 문으로 뛰쳐나간다.")
    time.sleep(2)

    VOICE("go_down", top_floor)
    time.sleep(2)
    print(f"\033[92m\033[40m[{top_floor}F]\033[0m")
    time.sleep(2)
    VOICE("open", top_floor)

    time.sleep(2)
    print(GUIDELINE[3])

    print("\n", GUIDELINE[32])
    print(f"당신은 \033[92m\033[40m {top_floor}층 \033[0m에 내려서 유리창을 찾는다.")
    time.sleep(1)
    print("\n ......")
    time.sleep(3)
    print("\n찾았다!")
    time.sleep(1)

    GLASS(top_floor)

    time.sleep(2)
    print()
    print(GUIDELINE[33])
    time.sleep(5)
    print("\n당신은 11번의 지시를 따라야 한다.\n")
    time.sleep(2)
    print(GUIDELINE[11])
    time.sleep(5)

    print(f"당신은 \033[92m\033[40m {top_floor}층 \033[0m에 멈춰있는 엘리베이터에 탄다.")
    time.sleep(2)
    print(GUIDELINE[112])
    time.sleep(7)

    print("당신은 반대편 거울을 마주보고 열림버튼을 누른다.")
    time.sleep(2)
    BUTTON("<>")
    time.sleep(1.5)
    print(end="\r")
    PRESS_BUTTON("<>")
    time.sleep(2)

    print("\n\033[1m\033[3m\033[37m쿵!\033[0m")
    time.sleep(2)
    print("\n거울안의 귀신이 다시 거울에 머리를 쳐박는다.\n")
    time.sleep(2)
    for i in range(lose_count*10):
        print("\033[1m\033[3m\033[37m나가고싶어" *7, "\n")
        time.sleep(1)
    print("\033[1m나가고싶어!!!!\033[0m")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)

    time.sleep(2)
    print("\n\033[92m삐익- 삐익- 삐익-\033[0m\n")
    time.sleep(2)
    print(GUIDELINE[113])
    time.sleep(2)

    PRESS_BUTTON("<>")
    time.sleep(2)
    print(end="\r")
    BUTTON("<>")
    print("\n")
    time.sleep(2)

    print("당신은 열림버튼에서 손을 뗀다.")
    time.sleep(2)
    print("....")
    time.sleep(2)
    print("당신은 망설인다.")
    input("1. 엘리베이터를 탄다.\n2. 계단을 찾는다.\n선택:")

    return




def end_w99():
    time.sleep(2)
    print("'거울 속 존재'가 웃는다.")
    time.sleep(1)
    print("당신은 이제 집으로 돌아 갈 수 없다.")
    time.sleep(2)
    print("\n행운을 빈다")
    time.sleep(2)

    print("\n당신은 무심코 엘리베이터의 거울을 쳐다본다.")
    time.sleep(2)

    print("\033[40m                                                                  \033[0m\n" * 40,
          "\033[40m                                                                  \033[0m", end="")

    time.sleep(2)

    print(end="\r")
    print("\033[40m ㅁㅁㅁㅁㅁ!! ㅁㅁㅁㅁㅁ!! ㅁㅁ..ㅁㅁ..                                \033[0m")

    time.sleep(2)

    print("                                                                  \n" * 40)

    time.sleep(2)

    print("열림버튼을 누르고 엘리베이터 안을 빠져 나가 계단으로 내려간다.")
    time.sleep(2)
    print(".....")
    time.sleep(2)
    print("지시사항을 99번까지 내린다.")
    time.sleep(2)
    print(GUIDELINE[99])
    time.sleep(2)
    print("'나'는 길게 웃으며 집으로 향한다.")
    time.sleep(2)
    print("\033[1mQterw-D-718", end="")
    time.sleep(2)
    print("\033[91m [거울을 보지 마세요]\033[0m")
    time.sleep(3)
    print("\n")
