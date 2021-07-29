# Numpy의 기본연산
# 배열에대한 기본적인 사칙연산을 제공
import numpy as np
array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

# 더하기
result_array = array + 10
#print(result_array)
# 빼기
result_array = array - 10
# print(result_array)
# 곱하기
result_array = array * 10
# print(result_array)
# 나누기
result_array = array / 10
# print(result_array)

# 서로다른 형태의 Numpy 연산 (numpy는 브로드캐스트를 지원)
# 2*2 + 1*2 하면 1*2배열이 2*2로 복사가 되서 연산을 수행 (행 우선으로 수행)
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)
# 브로드캐스트 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array3 = array1 + array2
print(array3)

array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(0, 4).reshape(4, 1) # (4 X 1)
print(array3 + array4)


# Numpy의 마스킹 연산
# 마스킹 : 각 원소에 대하여 체크함
array1 = np.arange(16).reshape(4, 4)
print(array1)
array2 = array1 < 10
print(array2)

# array1에서 True인 값을 100으로 변환
# 이미지데이터를 다룰때 픽셀이 너무 밝거나 하는값만 다른 픽셀로 바꿀때 사용
array1[array2] = 100
print(array1)

# Numpy의 집계함수
array = np.arange(16).reshape(4, 4)
print('최대값 : ', np.max(array))
print('최초값 : ', np.min(array))
print('합계 : ', np.sum(array))
print('평균값 : ', np.mean(array))

print(array)
# 열을 기준으로 모든행을 더한값
print('합계 : ', np.sum(array, axis=0))