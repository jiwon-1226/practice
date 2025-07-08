# 1부터 10까지의 숫자 중 짝수만 출력하는 파이썬 코드를 작성하세요

for i in range(2,10,2):
    print(i)

# 1부터 50까지의 숫자 중에서, 3의 배수이거나 5의 배수인 숫자들을 모두 더하는 프로그램을 작성하세요. 그리고 그 합을 출력하세요

total = 0
for i in range(1,50):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
