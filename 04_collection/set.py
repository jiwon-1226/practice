#세트
from pdb import line_prefix
from platform import java_ver

fruits = {"사과", "바나나", "오렌지", "바나나"}
print(fruits)
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers) #중복은 제거

empty_dit = {} #빈 딕셔너리 형태

empty_set = set() #빈 세트

#요소 추가
s = {1, 2, 3}
s.add(4) #한 개만 추가 할때
print(s)

s.update([5, 6, 7]) #여러개 한 번에 추가
print(s)

#요소 삭제
# s.remove(9) #존재하지 않는 값 제거 오류 발생
s.discard(10) #존재하지 않는 값 제거 오류 없음
print(s)

s.clear()
print(s)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B) #중복 제거, 합집합
print(A.union(B))

print(A & B) #교집합
print(A.intersection(B))

print(A - B) #차집합
print(A.difference(B))

#실습
pyton_class = {"철수", "영희", "민수", "지수"}
java_class = {"영희", "민수", "지훈", "길동"}

#파이썬가 자바 수업을 듣는 사람
print("둘다 듣는 사람 : ", pyton_class.intersection(java_class))
#파이썬만 듣는 사람
print("파이썬만 듣는 사람 : ", pyton_class - java_class)
#자바만 듣는 사람
print("자바만 듣는 사람 : ", java_class - pyton_class)
