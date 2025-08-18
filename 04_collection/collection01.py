#list
from operator import index
from pdb import line_prefix
from sys import prefix

# fruits = ["apple", "banana", "cherry"] #문자열 리스트
# number = [1, 2, 3, 4, 5] #숫자 리스트
# bools = [True, True, False, True, False] #불리언 리스트
# mixed_list = ["안녕하세요", 42, 3.14, "python", True] #혼합사용 가능
#
# #요소 접근 (인덱스)
# print(fruits[0]) #요소 하나하나당 번호
# print(fruits[0][0]) #첫번째 요소의 첫번째 인덱스
# print(number[-1])
#
# #요소 변경
# fruits[1] = "blueberry"
# print(fruits)
#
# #요소 추가
# fruits.append("grape") #마지막에 추가
# fruits.insert(1, "mango") #특정 위치에 추가
# print(fruits)
#
# #리스트 더하기
# list1 = ["A", "B", "C"]
# list2 = ["D", "E"]
# print(list1 + list2)
#
# #리스트 곱하기
# print(list1 * 3)
#
# #리스트에 여러요소 추가
# list1.extend(list2)
# print(list1)
#
# #리스트 삭제
# fruits.remove("cherry") #특정값을 삭제
# fruits.pop() #특정 인덱스로 삭제, 인덱스 생략시 마지막 요소 삭제
# del fruits[2] #"
# print(fruits)
#
# #리스트 길이
# print(len(fruits))
#
# #리스트 슬라이싱
# print(number[1:4])
# print(number[::-1])
#
# #리스트 정렬
# number.sort() #기본적으로 오름차순 정렬
# print(number)
# number.sort(reverse=True) #내림차순 정렬
# print(number)
# list1.sort(reverse=True)
# print(list1)
# kor = ["가", "나", "다"]
# kor.sort(reverse=True) #한글도 가능
# print(kor)
#
# number2 = sorted(number) #원본 변수에는 영향x, 새롭게 변수에 값을 할당
#
# #요소 존재 체크
# print("apple" in fruits)
#
# #리스트 요소 이어붙이기
# result = "-".join(list1)
# print(result)
#
# #리스트 실습
# cart = []
# #3개의 상품명을 입력받아서 cart에 추가
# #최종적으로 cart를 출력
# # c = [input("상품명 : ")]
# # cart.extend(c)
# # print(cart)
#
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
#
# print(cart)


#튜플(소괄호를 사용)
colors = ("r", "b", "g")
numbers = (1, 3, 6, 7, 9)
mixed = ("p", 43, True)
single_tuple = ("hello",) #요소가 1 개일 때는 꼭 ,를 붙여줘야함'
alphabet = ("a", "a", "a", "b", "c", "c")

#요소 접근
print(colors[1])

#요소 변경 불가
# colors[1] = "y"

#튜플 슬라이싱
print(colors[:2])
print(colors[::-1])

#count
print(alphabet.count("a"))

#index
print(alphabet.index("b"))

#튜플 언패킹
a, b, c = colors
print(a, b, c)



















