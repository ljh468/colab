import numpy as np



array1 = np.arange(0, 4).reshape(2, 2)
array2 = np.arange(0, 4).reshape(2, 2)
print(array1)
print(array2)
print(np.matmul(array1, array2))