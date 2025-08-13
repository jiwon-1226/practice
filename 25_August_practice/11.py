# #2. 숫자 맞추기 게임
# # 컴퓨터가 랜덤으로 고른 숫자를 사용자가 맞추는 게임입니다.
#
# import random
#
# def guss_num():
#     com_num = random.randint(1, 100)
#     while True:
#         try:
#             my_num = int(input("숫자를 입력하시오"))
#         except ValueError:
#             print("다시 입력하시오")
#             continue
#         if my_num > com_num:
#             print("down")
#         elif my_num < com_num:
#             print("up")
#         else:
#             print("정답!")
#             break
# guss_num()

#
# 3. 할 일 목록(To-Do List)
# 간단한 콘솔 기반 할 일 관리 프로그램입니다.

todo_list = []

def show_list():
    print("\n1. 할 일 입력하기")
    print("2. 할 일 목록보기")
    print("3. 종료")


def do():
    while True:
        show_list()
        do = int(input("번호를 입력하세요 : "))
        if do == 1:
            list = input("할 일을 입력하세요 : ")
            todo_list.append(list)
            print("할 일이 추가되었습니다")
        elif do == 2:
            for i, list in enumerate(todo_list, 1):
                print(f"{i}. {list}")
        elif do == 3:
            print("종료")
            break
        else:
            print("잘못된 입력입니다")

do()


















