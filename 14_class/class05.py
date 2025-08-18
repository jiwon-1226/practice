# Account 클래스 => 계좌 정보
# owner 그리고 balance => 잔액을 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
# withdraw 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
# 만약 잔액이 부족하다면 출금을 할 수 없도록 출력

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}님의 계좌가 개설되었습니다. 잔액:{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다\n잔액이 {self.balance}원 남았습니다.")
        else:
            print("입금액은 0보다 커야합니다.")


    def withdraw(self, amount):
        self.balance -= amount
        if amount <= 0:
            print("0보다 큰 수를 입력해주세요")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다\n잔액이 {self.balance}원 남았습니다.")
        else: #출금액이 0 이상이면서 잔액보다 출금액이 많은 상황
            print("잔액이 부족합니다")



account1 = Account("김지원")
account1.deposit(6450000)
account1.withdraw(5463)