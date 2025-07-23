# # requests 모듈
# # requests는 python에서 HTTP 요청을  보내는 데 사용되는 라이브러리다.
# import requests
#
# response = requests.get("https://www.naver.com/")
# print(response.status_code) #웹서버로부커 받은 응답의 HTTP 상태 코드를 출력
# print(response.text)
#
# # pandas 모듈
# import pandas as pd
# df_data = pd.read_csv("data.csv")
# # print(df_data)
# print(df_data.describe())
# """
# count 해당 열의 데이터 개수
# mean 평균값
# std 표준 편자 (데이터의 분산 정도)
# min 최솟값
# 25% 1사분위(25% 지점)
# 50% 중앙값 (50% 지점, 중위수)
# 75% 3사분위 (75% 지점)
# max 최댓값
# """
#
# print(df_data["Age"])
# print(df_data[["Age", "Salary"]]) #두 개 이상일 때는 한 번 더 감싸기
#
# #matplotlib
# #python에서 정적인, 애니메이션화된, 그리고 상호작용하는 시각화를 만드는데 사용된다
# import matplotlib.pyplot as plt
# df_data.groupby("Age")["Salary"].mean().plot(kind="bar")
# #df_data를 "Age" 칼럼으로 그룹화하고 각 연령대별로 "Salary"의 평균을 막대 그래프로 그린다
# plt.title("연령별 평균 연봉") #그래프이 제목
# plt.show() #그래프를 화면에 표시
# # pandas는 데이터 조작 및 분석을 위한 라이브러리
# # CSV, EXEL, 데이터 베이스 등 다양한 형식의 데이터를 읽고 쓸수 있으며,
# # 데이터를 정렬,필터링, 그룹화하는 기능을 제공한다
#

#numpy
#numpy는 python에서 수치계산, 특히 다차원 배열을 다루는데 핵심적인 라이브러리
#빠르고 효율적인 배열을 제공하여 과학, 공학 분야에서 복잡한 수학적 계산을 수행하는데 필수적이다
#백터, 행렬 등 선형 대수학 연산에 최적화 되어있다
import numpy as np

#1차원 배열
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

#2차원 배열
arr2 = np.array([[1, 2, 3],[4, 5, 6]])
print(arr2)

#1로 다 채운 다차원 배열
ones = np.ones((2, 3))
print(ones)

#0으로 다 채운 다차원 배열
zeros = np.zeros((3, 4))
print(zeros)

#특정한 값으로 채운 다차원 배열
filled = np.full((3,3), 7)
print(filled)

#연속된 값으로 채운 다차원 배열
arr_arange = np.arange(1, 10,)




