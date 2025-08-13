import pandas as pd
import requests
import numpy as np

# response = requests.get("https://www.naver.com")
# print(response.text)

a = np.array([1,2,3])
b = np.array([4,5,6])
print("a:", a)
print("b:", b)
print()

array_addition = a + b
print("각 행끼리 덧셈:", array_addition)

array_subtraction = a - b
print("각 행끼리 뺄셈:", array_subtraction)

array_multiplication = a * b
print("각 행끼리 곱셈:", array_multiplication)

array_division = a / b
print("각 행끼리 나눗셈:", array_division)

print()

matrix_a = np.array([[1,2], [3,4]])
matrix_b = np.array([[5,6], [7,8]])
matrix_multiplication = np.dot(matrix_a, matrix_b)
print(matrix_multiplication)

a = np.array([1,2,3])
b = np.mean(a)

print(a)
print(b)


# melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# melbourne_data = pd.read_csv(melbourne_file_path)
# melbourne_data.describe()

