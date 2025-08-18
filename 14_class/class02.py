
class Player:  #클래스 명은 대문자로 시작할 것
    def __init__(self, nickname, hp=100, gold=0, level=1): #기본값 설정이 안된 것 먼저 적기 = 필수값
        #nickname은 필수값, 나머지는 기본값
        self.nickname = nickname
        self.hp = hp
        self.gold = gold
        self.level = level
        print(f"닉네임:{self.nickname}\nHP: {self.hp}\nGOLD:{self.gold}\nLEVEL:{self.level}")

    def __del__(self):
        print("저장중...")
        print("저장되었습니다")

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname
        print(f"{self.nickname}으로 바뀌었습니다.")
        #현재 객체의 nickname 속성을 새로운 닉네임으로 변경


player1 = Player("모험가")
player1.change_nickname("모험가2")
print("player의 현재 닉네임:", player1.nickname)


