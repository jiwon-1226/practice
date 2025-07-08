#조건문
"""
if 조건:
    실행할 코드
"""

# num = int(input("숫자를 입력하세요 : "))
# if num > 0:
#     print("양수 입니다")
# else:
#     print("이 숫자는 0이거나 음수입니다")
#
# #if-elif-else문
# score = int(input("점수를 입력하세요 : "))
# if score >= 90:
#     print("A학점입니다")
# elif score >= 80:
#     print("B학점입니다")
# elif score >= 70:
#     print("C입니다")
# elif score >= 60:
#     print("D입니다")
# else:
#     print("F학점입니다")
#
# #실습
# #숫자를 입력 받아서 조건문으로 홀짝 판별
# n = int(input("숫자를 입력하세요 : "))
# if n % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")
#
#나이를 입력받고 학생여부 이력받기(y/n)
#20세 이상이면서 성인이면 성인학생입니다.
#아니면 설인학생 아닙니다.
age = int(input("나이를 입력하세요 : "))
student = input("학생여부를 입력하세요(y/n) : ")

if age >= 20 and student == "y":
    print("성인학생입니다")
else:
    print("성인학생 아닙니다")












