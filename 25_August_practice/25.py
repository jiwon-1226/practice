# import pygame as pg
#
# pg.init()
#
# # Define the colors we will use in RGB format
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# size = [400, 300]
# screen = pg.display.set_mode(size)
#
# pg.display.set_caption("Game Title")
#
#
# pg.draw.line(screen, GREEN, [0, 0], [100,150], 5)
# pg.draw.line(screen, BLUE, [0, 300], [100,150], 5)
#
#
# print("")

#숫자 맞추기 게임

import random

class Number_guess():
    def __init__(self, low=1, high=100, max_try=7):
        self.low = low
        self.high = high
        self.max_try = max_try
        self.answer = random.randint(low, high)
        self.tries = 0

    def guess(self, n: int):
        if self.tries >= self.max_try:
            return f"기회 소진! 정답: {self.answer}"
        self.tries += 1

        if n == self.answer:
            return f"정답! 정답: {self.answer}, {self.tries}번만에 맞췄습니다."

        hint = "high" if n < self.answer else "low"
        left = self.max_try - self.tries
        return f"{hint} (남은 기회:{left})"

def play():
    game = Number_guess()
    print("[숫자 맞추기] ")
    while game.tries < game.max_try:
        try:
            n = int(input("숫자를 입력해주세요:"))
        except ValueError:
            print("숫자를 입력해주세요")
            continue
        m = game.guess(n)
        print(m)
        if "정답!" in m:
            break

    else:
        print(f"실패! 정답은 {game.answer}")

if __name__ == "__main__":
    play()
    pass




