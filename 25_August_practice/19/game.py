
import time
import random


words = ["consequential", "resume", "conduct", "qualification", "essential"]

def my_game(is_player=True):
    time.sleep(2)
    print("======단어를 선택하고 있습니다=======")
    time.sleep(3)
    word = random.choice(words)
    blank_count = len(word) + 1
    print(f"{blank_count}개의 단어입니다")
    print("_" * blank_count)
    print(word)
    time.sleep(1)
    print("단어를 맞춰봅시다")
    while is_player:
        my_a = input("단어를 작성해주세요 : ")
        if my_a in word is True:
            print("와! 맞아요!")





