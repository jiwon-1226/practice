#배스킨라빈스

import random


player = ["컴퓨터", "플레이어"]
number = 0

def com_ch(num):
    com_choice = random.randint(1,3)
    if com_choice == 1:
        num += 1
        print(num)
    elif com_choice == 2:
        num += 1
        print(num)
        num += 1
        print(num)
    else:
        num += 1
        print(num)
        num += 1
        print(num)
        num += 1
        print(num)
    game(num)




def my_ch(num):
    while True:
        my_choice = []
        try:
            my_choice = list(map(int, input("연속된 숫자를 입력(3개 이하): ").split()))
        except ValueError:
            print("문자말고 숫자를 입력하시오")

        #개수 확인
        if not len(my_choice) <= 3:
            print("잘못된 입력입니다")
            continue

        #연속성 확인
        if not all(my_choice[i] + 1 == my_choice[i+1] for i in range(len(my_choice)-1)):
            continue

        # 시작 숫자 확인
        if my_choice[0] != num + 1:
            print(f"{num + 1}부터 시작해야 합니다.")
            continue

        # 입력 처리
        for n in my_choice:
            print(n)
            num = n
            if num >= 31:
                print("Game Over! 컴퓨터 승리!")
                return num

        return num


def game():
    # 시작하는 사람 정하기
    global number
    first = random.choice(player)
    print(f"{first}가 먼저 시작합니다")
    while number < 31:
        if first == "컴퓨터":
            number = com_ch(number)
            if number >= 31: break
            number = my_ch(number)
        else:
            number = my_ch(number)
            if number >= 31: break
            number = com_ch(number)


game()