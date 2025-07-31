# 숫자 짝수/홀수 판별기 만들기
# 사용자로부터 숫자를 입력받아 짝수인지 홀수인지 출력하는 프로그램을 작성하시오.
# 힌트: input(), int(), % 사용

num1 = int(input("숫자를 입력하시오:"))
num1 %= 2
if num1 == 0:
    print("짝수")
else:
    print("홀수")


# 1부터 100까지의 합 구하기
# for문 또는 while문을 사용하여 1부터 100까지의 합을 계산하는 프로그램을 작성하시오.

#for
total = 0
for i in range(1, 101):
    total += i
print(total)

#while
num = 0
t_num = 0
while num <= 100:
    t_num += num
    num += 1
while num > 100:
    break
print(t_num)

# 단어 거꾸로 출력하기
# 사용자에게 단어를 입력받고, 그것을 거꾸로 출력하시오.
# 예: apple → elppa

word = input("단어를 입력하세요: ")
