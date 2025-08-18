#딕셔너리

profile = {
    "이름": "김지원",
    "나이": 21,
    "취미": ["영화", "야구"],
    2: 3,
    4: [1, 2, 3]
}

#요소 접근
print(profile["이름"])
print(profile["취미"][1])

#수정
profile["나이"] = 22
print(profile)

#요소 추가
profile["직업"] = "강사"
print(profile)

#요소 삭제
del profile["직업"]
print(profile)
# profile.clear() #전체 삭제

#키만 불러오기
print(profile.keys())

#값만 불러오기
print(profile.values())

#키와 값 둘 다 불러오기
print(profile.items())

python_grade = {
    "kelly": "B",
    "jason": "A",
    "ian": "C",
    "elly": "D"
}

print(sorted(python_grade.items())) #키 기준 오름차순 정렬
print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순 정렬

student = {}
#이름을 입력받고 해당 이름을 킬, 점수를 입력받고 값을 추가
#student = {"김지원": 80}

name = input("이름 : ")
sore = input(f"{name}의 점수 : ")
student[name] = sore
print(student)


