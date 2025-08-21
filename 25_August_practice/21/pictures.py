REPAIR = """
＿＿＿＿＿=====＿＿＿＿＿
|     -수리 중-       |
|  빠르게 고치겠습니다. |
| 행복나라아파트 경비실 |
|＿＿＿＿＿＿＿＿＿＿＿＿|
""", """
＿＿＿＿＿=====＿＿＿＿＿
|     -수리 중-       |
|  빠르게 고치겠습니다. |
|   ^^해피타워 경비실  |
|＿＿＿＿＿＿＿＿＿＿＿＿|
""", """
＿＿＿＿＿=====＿＿＿＿＿
|     -수리 중-       |
|  빠르게 고치겠습니다. |
|  ()()아파트 경비실   |
|＿＿＿＿＿＿＿＿＿＿＿＿|
"""


def ELEVATOR(instrution, floor):
    if instrution == "close":
        print(" ＿＿＿＿＿＿＿＿＿＿＿＿＿\n"
              f"|    \033[92m\033[40m [{floor}F] \033[0m     |\n"
              "|  ＿＿＿＿＿＿＿＿＿＿   |\n"
              "|  |       |       |  |\n"
              "|  |       |       |  |\n"
              "|  |       |       |  |\n"
              "|  |       |       |  |\n"
              "|  |       |       |  |\n"
              "=======================\n", end="")

    elif instrution == "close_repair":
        print(" ＿＿＿＿＿＿＿＿＿＿＿＿＿\n"
              f"|    \033[92m\033[40m [{floor}F] \033[0m     |\n"
              "|  ＿＿＿＿＿＿＿＿＿＿   |\n"
              "|  |       |       |  |\n"
              "|  |  ___  |       |  |\n"
              "|  | |___| |       |  |\n"
              "|  |       |       |  |\n"
              "|  |       |       |  |\n"
              "=======================\n", end="")
    elif instrution == "opening":
        print(" ＿＿＿＿＿＿＿＿＿＿＿＿＿\n"
              f"|    \033[92m\033[40m [{floor}F] \033[0m     |\n"
              "|  ＿＿＿＿＿＿＿＿＿＿   |\n"
              "|  |    |     |    |  |\n"
              "|  |    |     |    |  |\n"
              "|  |    |     |    |  |\n"
              "|  |    |     |    |  |\n"
              "|  |    |     |    |  |\n"
              "=======================\n", end="")
    elif instrution == "open":
        print(" ＿＿＿＿＿＿＿＿＿＿＿＿＿\n"
              f"|    \033[92m\033[40m [{floor}F] \033[0m     |\n"
              "|  ＿＿＿＿＿＿＿＿＿＿   |\n"
              "|  |               |  |\n"
              "|  |               |  |\n"
              "|  |               |  |\n"
              "|  |               |  |\n"
              "|  |               |  |\n"
              "=======================\n", end="")
    elif instrution == "opening_with_hand":
        print(" ＿＿＿＿＿＿＿＿＿＿＿＿＿\n"
              f"|       \033[92m\033[40m [{floor}F] \033[0m        |\n"
              "|  ＿＿＿＿＿＿＿＿＿＿   |\n"
              "|  |    |     |    |  |\n"
              "|  |    |     |    |  |\n"
              "|  |    |_    |    |  |\n"
              "|  |    |//   |    |  |\n"
              "|  |   🤚\uFE0E      |    |  |\n"
              "========================\n")

mirror_pic = ["＿＿＿＿＿＿＿＿＿＿＿＿＿",
              "|                    |",
              "|      (' - ')       |",
              "|      __| |__       |",
              "|     /     O |      |",
              "|＿＿_/＿＿＿＿\\|＿＿＿＿|"
              ]

face_pic = ["|      (' v ')       |",
            "|      (' U ')       |",
            "|      (' n ')       |",
            "|      (` д ´)       |",
            ]
rsp_pic = ["|     /     ✊\uFE0E|      |",
           "|     /     ✋\uFE0E|      |"]

def MIRROR(choice, face):
    print(mirror_pic[0])
    print(mirror_pic[1])
    #거울 속 표정
    if face == "좋음":
        print(face_pic[0])
    elif face == "매우좋음":
        print(face_pic[1])
    elif face == "나쁨":
        print(face_pic[2])
    elif face == "매우나쁨":
        print(face_pic[3])
    else:
        print(mirror_pic[2])
    print(mirror_pic[3])
    #거울의 손동작
    if choice == "r":
        print(rsp_pic[0])
    elif choice == "p":
        print(rsp_pic[1])
    else:
        print(mirror_pic[4])
    print(mirror_pic[5])


