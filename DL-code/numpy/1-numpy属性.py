import numpy as np

array = [[1, 2, 3],
         [4, 5, 6]]

array = np.array(array)                            # 列表数组化

print(array)
print('the number of dim:', array.ndim)            # 维度
print('the shape of array:', array.shape)          # 数组形状
print('the size of array:', array.size)            # 数组大小
