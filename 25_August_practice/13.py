# 8. 블랙잭 카드 게임 (난이도 ★★★)
# 컴퓨터(딜러)와 사용자 카드 합이 21에 가까운 쪽이 승리
#
# 카드 뽑기(Hit) / 멈추기(Stand) 기능 구현
#
# A(에이스)는 1 또는 11로 계산

"""
금액 : 처음 가지고 있는 금액은 500불
계산
-내추럴 블랙잭: 1.5배
-버스트(bust): 21점 초과, 전액 잃음
-스탠드(stand): 플레이어가 더 이상 추가 카드를 원하지 않을때. 딜러는 17이상의 수가 나오면 추가 카드 받지 않기
-힛(hit): 플레이어가 처음 두장의 카드 이외의 추가카드를 요청할 때
-스플릿(split): 처음 받은 두장의 카드가 같을 경우 두 카드를 나눠서 각각 배팅. 배팅하는 금액은 처음 배팅한 금액과 동일해야함
-푸쉬(push): 플레이어의 합과 딜러의 합이 같을 경우

"""

import random
import time
import sys

print("====== 블랙잭 =======")

money = 500

def betting():
    while True:
        mymoney = money
        bet = int(input("보유 금액: 얼마를 베팅하시겠습니까 :"))
        if mymoney >= bet:
            mymoney -= bet
            print(f"{bet}불 베팅하셨습니다. {mymoney}불 남았습니다.")
            first_game()
            break
        else:
            print(f"잔액이 부족합니다. 보유금액: {mymoney}불")
            continue

cards = [
        "클로버_A", "클로버_2", "클로버_3", "클로버_4", "클로버_5", "클로버_6", "클로버_7", "클로버_8", "클로버_9", "클로버10", "클로버_J", "클로버_Q", "클로버_K",
        "다이아_A", "다이아_2", "다이아_3", "다이아_4", "다이아_5", "다이아_6", "다이아_7", "다이아_8", "다이아_9", "다이아10", "다이아_J", "다이아_Q", "다이아_K",
        " 하트_A", " 하트_2", " 하트_3", " 하트_4", " 하트_5", " 하트_6", " 하트_7", " 하트_8", " 하트_9", " 하트10", " 하트_J", " 하트_Q", " 하트_K",
        "스페이드A", "스페이드2", "스페이드3", "스페이드4", "스페이드5", "스페이드6", "스페이드7", "스페이드8", "스페이드9", "스페이드10", "스페이드J", "스페이드Q", "스페이드K"
    ]

def card_value(card_name, is_player=True):
    rank = card_name.split("_")[1]  # 예: "A", "10", "K"

    if rank == "A":
        if is_player:
            while True:
                choice = input(f"{card_name} - 1로 하시겠습니까, 11로 하시겠습니까? : ")
                if choice in ["1", "11"]:
                    return int(choice)
                else:
                    print("1 또는 11만 입력하세요.")
        else:
            return 11  # 딜러는 기본적으로 A를 11로
    elif rank in ["K", "Q", "J"]:
        return 10
    else:
        return int(rank)

def result(score, is_player=True):
    global money
    if score == 21:
        if is_player == True:
            print("Black Jack! you win!")
            money *= 1.5
            print(f"현재 금액 : {money}")
        else:
            print("Black Jack for dealer, you lose")
            print(f"보유 금액: {money}")
            game_over()
    elif score > 21:
        if is_player == False:
            print("dealer's card is over 21! you win")
            money += 1.2
            print(f"보유금액 : {money}")
        else:
            time.sleep(2)
            print("Bust!!\nYour card is over 21! you lose")
            print(f"보유금액 : {money}")
    else:
        if is_player == False:
            if score >= 17:
                return com_score
            else:
                com_third = str(random.choice(deck))
                deck.remove(com_third)
                print(f"컴퓨터 세번째 카드: {com_third}")

                com_score = score + card_value(com_third, False)
                result(com_score)
                return com_score
        else:
            first_game_next(score, True)




def game_over():
    print("게임 종료")
    sys.exit()


def first_game():
    deck = cards.copy()

    print("첫번째 카드 베팅중...")
    time.sleep(2)

    com_first = str(random.choice(deck))
    deck.remove(com_first)
    print(f"컴퓨터 첫번째 카드: {com_first}")


    time.sleep(1)

    my_first = str(random.choice(deck))
    deck.remove(my_first)
    print(f"내 첫번째 카드: {my_first}")

    print("두번째 카드 베팅중...")
    time.sleep(2)

    com_second = str(random.choice(deck))
    deck.remove(com_second)

    my_second = str(random.choice(deck))
    deck.remove(my_second)
    print(f"내 두번째 카드: {my_second}")

    time.sleep(1)
    print("카드 베팅이 완료되었습니다.")


    my_score = card_value(my_first) + card_value(my_second)
    com_score = card_value(com_first, False) + card_value(com_second, False)

    result(my_score)
    result(com_score,False)

def first_game_next(score):
    while True:
        global deck
        choice = input("Hit or Stand?!\n\n1. hit \n2. Stand \n선택 : ")
        if choice == 1:
            print("세번째 카드 베팅중...")
            time.sleep(2)

            my_third = str(random.choice(deck))
            deck.remove(my_third)
            print(f"내 세번째 카드: {my_third}")

            time.sleep(1)
            print("카드 베팅이 완료되었습니다.")

            my_score = score + card_value(my_third)
            result(my_score)
        elif choice == 2:
            print("카드값을 계산합니다...")
            time.sleep(2)
            pass

        else:
            print("다시 숫자를 입력해주세요")
            continue

betting()

# #각종 문자열 함수
# a = "Life is too short, You need Python"
# print(len(a)) #해당 문자열의 길이
# print(a.count("t")) #특정 문자가 몇개 있는지
# print(a.index("t")) #특정 문자의 인덱스 찾기
# print(a.index("t",10, 18))
# #특정문자, 시작 인덱스, 끝인덱스로 구간을 설정
# print(a.find("t"))  #특정문자 시작 끝 구간 설정 가능
