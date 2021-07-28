import numpy as np
list_data = [1,2,3]
array = np.array(list_data)
print(array)
print(array.size) # 사이즈 확인가능
print(array.dtype) # 데이터타입 확인가능
print(array[2]) # 인덱싱 가능
print(array[0:2]) # 슬라이싱 가능

# numpy는 리스트와 호환됨
# 랜덤한 데이터를 만들거나 행렬곱을 하거나 다양한 연산을 제공

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 0으로 초기화된 데이터 만들기
array2 = np.zeros((4,4), dtype=float) # 4*4 배열
print(array2)

# 1로 초기화된 데이터 만들기
array3 = np.ones((4,4), dtype=str)
print(array3)

# 0부터 9까지 랜덤값이 초기화된 데이터 만들기
array4 = np.random.randint(0,10,(3,3)) # 3*3 배열
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열 (표준정규분포)
array5 = np.random.normal(0, 1,(3, 3)) # 3*3 배열
print(array5)

# Numpy 배열 합치기 (concatenate)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate([arr1, arr2])
print(arr3)

# Numpy 배열 형태 바꾸기 (reshape)
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1.reshape((2,2))
print(arr2)

# Numpy 배열 세로축으로 합치기
# |1|2| + |3|4| = |1|2|
#                 |3|4|
arr1 = np.arange(4).reshape(1,4)
arr2 = np.arange(8).reshape(2,4)
arr3 = np.concatenate([arr1, arr2], axis=0) # axis=1은 행을 의미
print(arr3)

# Numpy 배열 나누기
array = np.arange(8).reshape(2,4)
left, right = np.split(array, [2], axis=1 ) # 인덱스2를 기준으로 axis=1은 열을 의미
print(left.shape)
print(right.shape)
print(array)
print(left)