#내장 함수
#파이썬에서 기본적으로 지원하는 함수 (built-in function)
from importlib.resources import contents
from pdb import line_prefix

#abs()
#숫자의 절댓값을 리턴하는 함수
print(abs(-10))
print(abs(-1.2))

#all()
#all(x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 false를 리턴
#모든 요소가 참인가?
num_list = [1, 2, 0, 4] #0은 false => 모두 참이 아님
print(all(num_list))
num_list = []
print(all(num_list))
#빈 리스트의 경우, 안에 어떤 요소도 존재하지 않음.
#따라서 "거짓인 요소가 하나라도 있는가?" => "거짓인 요소가 없다"
#거짓인 요소가 없기 때문에 모든 요소가 참이라는 조건에 위배되지 않는다

#any()
#any(x)는 반복 가능한 데이터 x를 입력값으로 받으면
#이 x의 요소가 하나라도 참이면 true, 요소가 모두 거짓이면 false
num_list = [1, 2, 0, 4]
print(any(num_list))
num_list = [0, 0, 0, 0]
print(any(num_list))

#chr()
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴하는 함수
print(chr(97)) #a
print(chr(44032)) #가


#dir()
#객체가 지닌 변수나 함수를 보여주는 함수
name = "python"
print(dir(name))

#divmod()
#2개의 숫자 a, b를 입력받고 그리고 a를 b로 나눈 몫과 나머지를 튜플형태로 리턴
print(divmod(7, 3))


#enumerate() *자주 쓰임
#순서가 있는 데이터(리스트, 튜플, 문자열)을 입력받아서 인덱스 값을 포함하는 enumerate 객체를 리턴
#인덱스와 값을 두 개의 변수로 언팩
a_list = ["name", "age", "birth"]

for i, value in enumerate(a_list):
    print(i, value)

for i, value in enumerate(a_list):
    print(f"{i+1}. {value}")

#eval()
#문자열로 구성되어있음. 해당 문자열을 실행한 값
a_str = "1 + 2"
print(eval(a_str)) #3
print(eval("divmod(7,2)"))

#filter() *자주 쓰임
#첫번째 인수로 함수, 두번째 인수로 반복가능한 데이터
#그리고 반복가능한 데이더의 요소 순서대로 함수를 호출햇을떼 리턴값이 참인것만 묶어서 리턴

def positive(x):
    return x > 0

print(list(filter(positive, [1, -2, 5, -3, 8])))

#hex()
#정수를 입력받아서 16진수 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(12))

# id()
#객체를 입력받아서 고유 주솟값(래퍼런스)를 리턴하는 함수
a = 3
print(id(a))

#map() *자주 쓰임
#map은 입력받은 데이터의 각 요소에 함수를 적용한 결과를 리턴하는 함수
#map(함수, 적용대상)
def two_time(x):
    return x * 2

print(list(map(two_time, [1, 2, 3, 4])))

#max()
#반복가능한 데이터 중에서 최댓값을 리턴
num_list = [1, 2, 13, 15, 23]
print(max(num_list))

#min()
#반복가능한 데이터 중에서 최솟값을 리턴
num_list = [1, 2, 13, 15, 23]
print(min(num_list))

#oct()
#정수를 8진수 문자열로 바꾸어 리턴하는 함수
print(oct(34))
print(oct(12345))

#open() *자주 쓰임
#open(file name, 모드)은 파일이름고 모드를 입력받아 파일 객체를 리턴하는 함수
# w 쓰기 모드
# r 읽기 모드
# a 추가 모드
file = open("예시.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

with open("예시.txt", "r", encoding="utf=8") as file:
    content = file.read()
    print(content) #따로 close 할 필요 없음

#ord() <=> chr()
#ord()는 문자의 유니코드 숫자 값을 리컨하는 함수
print(ord("가"))
print(ord("a"))

#pow()
#첫번째 인수의 두번 째 인수만틈 거듭제곱 한 값을 리턴
print(pow(3, 10))
print(pow(2, 10))

#range()
#range(시작, 끝, 간격) for문과 함께 자주 사용
#반복 가능한 객체로 만들어서 리턴
print(list(range(5, 100, 5)))

#round()
#반올림
print(round(4,4))
print(round(5.1284, 2)) #해당 자리만큼 나타내라

#sum()
#합계를 구하는 함수
num_list = [123, 5646, 616, 54]
print(sum(num_list))

#실습 문제
data = ["apple", "banana", "cherry", "grape", "mango", "blueberry", "lemon"]
#1. apple
#2. banana

for i, fruit in enumerate(data):
    print(f"{i+1}. {fruit}")

#인덱스가 짝수인 요소만 출력 (인덱스 : 요소)
for i, fruit in enumerate(data):
    if i % 2 == 0:
        print(f"{i} : {fruit}")
        print(f"인덱스:{i}, 값:{fruit}")