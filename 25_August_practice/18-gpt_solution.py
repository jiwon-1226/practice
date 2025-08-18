import random

player = ["컴퓨터", "플레이어"]
number = 0  # 현재 숫자

def com_ch(num):
    com_choice = random.randint(1, 3)  # 1~3개 부르기
    print("\n[컴퓨터의 차례]")
    for _ in range(com_choice):
        num += 1
        print(num)
        if num >= 31:
            print("Game Over! 플레이어 승리!")
            return num
    return num


def my_ch(num):
    print("\n[플레이어의 차례]")
    while True:
        try:
            my_choice = list(map(int, input("연속된 숫자(3개 이하): ").split()))
        except ValueError:
            print("잘못된 입력입니다. 숫자만 입력하세요.")
            continue

        # 입력 개수 확인
        if not (1 <= len(my_choice) <= 3):
            print("1개 이상, 3개 이하로 입력하세요.")
            continue

        # 연속성 확인
        if not all(my_choice[i] + 1 == my_choice[i+1] for i in range(len(my_choice)-1)):
            print("연속된 숫자를 입력해야 합니다.")
            continue

        # 시작 숫자 확인
        if my_choice[0] != num + 1:
            print(f"{num+1}부터 시작해야 합니다.")
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
    global number
    first = random.choice(player)
    print(f"👉 {first}가 먼저 시작합니다!")

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