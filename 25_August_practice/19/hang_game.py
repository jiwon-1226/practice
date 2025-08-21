import time
import random
from files import HANGMANGIVEN, HANGMANPICS, words
from hangman import game_over
import os




blank_answer = []
answer = []
player_guess_list = []

def my_game(hangman, is_player=True):
    over = 0
    time.sleep(2)
    print("\n======단어를 선택하고 있습니다=======\n")
    time.sleep(3)
    word = random.choice(words)
    blank_count = len(word)
    print(f"{blank_count}개의 단어입니다")

    for j in range(0, len(word)):
        blank_answer.append("_")
    for i in word:
        answer.append(i)
    print(answer)


    while over != 1:
        hangman_life = 7
        while True:
            print(HANGMANPICS[7 - hangman_life])
            if len(player_guess_list) == 0:
                pass
            else:
                print(f"Inferred Letter: {", ".join(player_guess_list)}")
                print(' '.join(blank_answer))
            while True:
                player_guess = input("Input letter > ").lower()
                if not player_guess.isalpha():
                    print("please write alphabet :)", end="")
                    time.sleep(3)
                    print(end="\r")
                    continue
                if len(player_guess) >= 2:
                    print("write just one letter")
                    time.sleep(3)
                    print(end="\r")
                    continue
                else:
                    break
            player_guess_list.append(player_guess)


            # 사용자가 유추한 글다 중 하나가 선택된 단어 안에 있으면 출력
            if player_guess in answer:
                print("맞았습니다!")
                num = 0
                for m in word:
                    if player_guess == m:
                        blank_answer[num] = m
                    num += 1
                print(blank_answer)
            else:
                print("틀렸습니다")
                hangman_life -= 1
                print(f"{hangman}의 {HANGMANGIVEN[7 - hangman_life]}가 쟁반에 올라갑니다")
            os.system("cls")

            if answer == blank_answer:
                print(f"맞췄습니다! 정답은 {word}!")
                os._exit(os.EX_OK)

            elif hangman_life == 0:
                print(HANGMANPICS[6])
                print(f"정답은 {word}! 아쉽지만 {hangman}은 사망하였습니다. \n{hangman}의 시체는 괴담에 귀속됩니다.")
                os._exit(os.EX_OK)

