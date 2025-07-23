# Account 클래스 => 계좌 정보
# owner 그리고 balance => 잔액을 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
# withdraw 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
# 만약 잔액이 부족하다면 출금을 할 수 없도록 출력


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num1):
        self.num1 = num1
        print(f"{self.num1}원이 입금되었습니다\n잔액이 {self.balance + self.num1}원 남았습니다.")


    def withdraw(self, num2):
        self.num2 = num2

        if num2 <= 0:
            print("0보다 큰 수를 입력해주세요")

        else num2 > balance

            print(f"{self.num2}원이 출금되었습니다\n잔액이 {self.balance - self.num2}원 남았습니다.")

account1 = Account("김지원", 465500)
account1.withdraw(2000)