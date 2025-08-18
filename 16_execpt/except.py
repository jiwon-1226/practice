#
# print(10/0)
from importlib.resources import contents
from pdb import line_prefix
#
# try:
#     print(10/0)
# except:
#     print("예외 발생")
#
# try:
#     num = int(input("숫자를 입력해주세요:"))
#     print(10/num)
# except ValueError: #값 데이터 오류
#     print("문자말고 숫자 넣")
# except ZeroDivisionError:
#     print("0 넣지 마라")

# #indexerror, ValueError
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스:"))
#     print(my_list[index])
# except ValueError:
#     print("숫자만")
# except IndexError:
#     print("인덱스")

# #파일 입출력 예외 처리: FileNotFoundError
# file = None
# try:
#     file = open("hi.text", "r", encoding="utf-8")
#     content = file.read() #파일의 내용을 읽어온다
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("그런 파일 없음")
# finally:
#     if file is not None and not file.closed:
#         file.close()
#         print("정상적으로 파일이 닫혔습니다")
#     elif file is None:
#         print("애초에 안열림")
#
# #리스트 요소 5개를 선언하고 index로 찾는 로직
# #indexError, ValueError 예외 처리
# #정상적이면 해당 리스트 값 출력
# #마지막은 항상 끝 출력
# list1 = [1, 2, 3, 4, 5, 7]
# try:
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     result = list1[index]
# except IndexError as message:
#     print("그런 인덱스 없음")
#     print(message)
# except ValueError as message:
#     print("숫자 입력바람")
#     print(message)
# else:
#     print(f"해당 인덱스의 값: {result}")
# finally:
#     print("끝")
#
#
# #raise 키워드 : 강제로 예외 발생시키기 (커스텀 예외 클래스)
# #특정 조건에서 개발자가 직접 예외를 발생시키는데 사용
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise Exception("0이상 150미만 숫자만 입력해주세요")
# except Exception as e:
#     print(e)
# else:
#     print(f"입력된 나이: {age}")
# finally:
#     print("끝")
#
# #사용자 정의 예외 클래스
# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150미만 숫자만 입력하시오")
#
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("end")

#출금을 할때 잔액이 부족하면 발생되는 에러
#FundsError -> 잔액이 부족합니다. 현재 잔액 ***원, 출금 시도 금액 ***원
#Account클래스 만들고 메소드 withdraw 출금
#출금을 할때 잔액이 부족하면 FundsError를 발생


class FundsError(Exception):
    def __init__(self, balance, amount): #생성자에서 현재 잔액과 출금시도 금액
        super().__init__(f"잔액이 부족합니다 현재 잔액 {balance}원, 출금 시도 금액 {amount}원")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def whithdraw(self, amount):
        try:
            if amount <= 0 or amount > self.balance:
                raise FundsError(self.balance, amount)
        except FundsError as e:
            print(e)
        else:
            self.balance -= amount
            print(f"정상적으로 출금되었습니다 남은 잔액 : {self.balance}")

account1 = BankAccount(10000)
account1.whithdraw(100000)

#딕셔너리 요소 찾기 (숙제)
#딕셔너리 키를 입력 받기 (숫자로)
#result 변수에 해당 키의 값으 넣음
#예외처리 => 해당 키가 존재하지 않을 때 "KeyError" 처리 : "해당 키믐 존재하지 않습니다" 출력
#숫자가 아닌 문자를 입력했을때 "ValueError" 처리 : "숫자를 입력해주세요"
#정상적으로 실행된다면 해당 키으 갑쇼을 넣어둔 result 출력
#마지막은 완료 출력

my_dict = {
    1: "사과",
    2: "바나나",
    3: "딸기",
    4: "포도",
    5: "수박"
}

try:
    key_input = input("딕셔너리에서 찾을 키를 입력해주세요 :")
    key = int(key_input) #ValueError가 발생할 수 있는 코드
    result = my_dict[key] #KeyError가 발생할 수 있는 코드
except ValueError:
    print("숫자를 입력해주세요")
except KeyError:
    print("해당키는 존재하지 않습니다")
else:
    print(result)
finally:
    print("완료")