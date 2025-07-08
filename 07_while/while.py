#반복문 while
"""
while 조건:
    반복할 코드
    (조건을 변경하는 코드)
"""

# num = 1
# while num <= 5:
#     print("숫자:", num)
#     num += 1

# num = 1
# while num <= 10:
#     print(num)
#
#     if num == 5: #num이 5가 되었을 때 반복 종류
#         break #반복을 종료하는 코드
#
#     num += 1

# num = 0
# while num < 10:
#     num += 1
#     if num % 3 == 0: #3의 배수를 건너 뜀
#         continue
#     print(num)

# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan} X {n} = {dan * n}")
#         n += 1
#     dan += 1

#실습
#1. 1부터 100까지 짝수만 출력하기

# num = 1
# while num <= 100:
#     num += 1
#     if num % 2 != 0:
#         continue
#     print(num)
#
# while num <= 100:
#     if num % 2 == 0:
#         print(num)
#     num += 1
#
# num1 = 2
# while num1 <= 100:
#     print(num1)
#     num1 += 2


#5의 배수 출력 50까지 (30에서 멈추기) - 숙제

num2 = 0
while num2 <= 50:
    print(num2)
    if num2 == 30:
        break
    num2 += 5







