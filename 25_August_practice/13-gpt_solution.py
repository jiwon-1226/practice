import random
import time

print("====== 블랙잭 =======")

cards = [
    "클로버_A", "클로버_2", "클로버_3", "클로버_4", "클로버_5", "클로버_6", "클로버_7", "클로버_8", "클로버_9", "클로버10", "클로버_J", "클로버_Q", "클로버_K",
    "다이아_A", "다이아_2", "다이아_3", "다이아_4", "다이아_5", "다이아_6", "다이아_7", "다이아_8", "다이아_9", "다이아10", "다이아_J", "다이아_Q", "다이아_K",
    "_하트_A", "_하트_2", "_하트_3", "_하트_4", "_하트_5", "_하트_6", "_하트_7", "_하트_8", "_하트_9", "하트_10", "_하트_J", "_하트_Q", "_하트_K",
    "스페이드A", "스페이드2", "스페이드3", "스페이드4", "스페이드5", "스페이드6", "스페이드7", "스페이드8", "스페이드9", "스페이드10", "스페이드J", "스페이드Q", "스페이드K"
]

def betting(money):
    while True:
        try:
            bet = int(input(f"보유 금액: {money}\n얼마를 베팅하시겠습니까 : "))
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if 0 < bet <= money:
            money -= bet
            print(f"{bet}불 베팅하셨습니다. {money}불 남았습니다.")
            return bet, money
        elif money == 0:
            print("돈을 모두 잃었습니다\n게임을 종료합니다")
            return 0, money
        else:
            print(f"잔액이 부족합니다. 보유금액: {money}불")

def card_value(card_name, is_player=True):
    rank = card_name[4]
    if rank == "A":
        if is_player:
            while True:
                choice = input(f"{card_name} - 1로 하시겠습니까, 11로 하시겠습니까? : ")
                if choice in ["1", "11"]:
                    return int(choice)
                else:
                    print("1 또는 11만 입력하세요.")
        else:
            return 11
    elif rank in ["K", "Q", "J"]:
        return 10
    elif rank == 0:
        return 10
    else:
        return int(rank)

def result(score, bet, money, is_player=True):
    if score == 21:
        if is_player:
            print("Black Jack! you win!")
            money += int(bet * 1.5)

        else:
            print("Black Jack for dealer, you lose")
    elif score > 21:
        if not is_player:
            print("dealer's card is over 21! you win")
            money += int(bet * 1.2)
        else:
            print("Bust!!\nYour card is over 21! you lose")
    return money

def stand(score1, score2, bet, money):
    print(f"Player's score : {score1}\nDealer's score : {score2}")
    if score1 > score2:
        print("You win!")
        money += int(bet * 1.2)
    else:
        print("You lose")
    return money

def first_game(bet, money):
    deck = cards.copy()

    # 첫 카드
    com_first = random.choice(deck)
    deck.remove(com_first)
    print(f"컴퓨터 첫번째 카드: {com_first}")

    my_first = random.choice(deck)
    deck.remove(my_first)
    print(f"내 첫번째 카드: {my_first}")

    # 두 번째 카드
    com_second = random.choice(deck)
    deck.remove(com_second)

    my_second = random.choice(deck)
    deck.remove(my_second)
    print(f"내 두번째 카드: {my_second}")

    my_score = card_value(my_first) + card_value(my_second)
    com_score = card_value(com_first, False) + card_value(com_second, False)

    money = result(my_score, bet, money, True)
    money = result(com_score, bet, money, False)

    while True:
        choice = input("Hit or Stand?!\n\n1. hit \n2. Stand \n선택 : ")
        if choice == "1":
            my_third = random.choice(deck)
            deck.remove(my_third)
            print(f"내 세번째 카드: {my_third}")
            my_score += card_value(my_third)
            money = result(my_score, bet, money, True)
        elif choice == "2":
            money = stand(my_score, com_score, bet, money)
            break
        else:
            print("다시 숫자를 입력해주세요")
    return money

def main():
    money = 500
    while money > 0:
        bet, money = betting(money)
        if bet == 0:  # 돈이 없음
            break
        money = first_game(bet, money)
        print(f"현재 보유금액: {money}")

    print("게임 종료")

if __name__ == "__main__":
    main()