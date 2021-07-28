# Numpy의 활용
import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy', array)
result = np.load('saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz', array1= array1, array2=array2)
data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']

print(result1)
print(result2)

# Numpy 원소의 정렬
# |9|2|7|5|6|8|1|4|3|0|
# |0|1|2|3|4|5|6|7|8|9|

# Numpy 원소 오름차순 정령
array = np.array([5, 9, 10, 3, 1])
array.sort()
print(array)
# 내림차순
array2 = array[::-1] # 역순으로
print(array2)

# 각 열을 기준으로 정령
array = np.array( [ [5, 9, 10, 3, 1], [8, 3, 4, 2, 5] ] )
print(array)
array.sort(axis=0)
print(array)

# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5) # 처음값, 끝값, 사이의 값개수
print(array)

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3))) # 처음값, 끝값, 2*3배열

# Numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
# array2가 변화가 되면 array1도 변화가 됨 (array1, array2는 값은 주소를 가리킴)
print(array1)
# 이것을 방지하기위해 복사해서 사용
array1 = np.arange(0, 10)
array2 = array1.copy()
array2[0] = 99
print(array1)

# 중복된 원소 제거
array = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array))