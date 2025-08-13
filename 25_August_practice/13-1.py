



#각종 문자열 함수
a = "Life is too short, You need Python"
print(len(a)) #해당 문자열의 길이
print(a.count("t")) #특정 문자가 몇개 있는지
print(a.index("t")) #특정 문자의 인덱스 찾기
print(a.index("t",10, 18))
#특정문자, 시작 인덱스, 끝인덱스로 구간을 설정
print(a.find("t"))  #특정문자 시작 끝 구간 설정 가능
