import numpy as np

A = np.arange(3, 15).reshape((3, 4))                    # 各种根据索引进行访问数组和矩阵的方法
print(A)
print(A[2])
print(A[2, :])
print(A[:, 2])
print(A[1, 1:3])
print(A[2][2])
print(A[2, 2])


print(A)
for row in A:                                           # 按行进行遍历
    print(row)

for column in A.T:                                      # 按列进行遍历
    print(column)

print(A)
print(A.flatten())                                      # 矩阵一维向量化

for item in A.flat:                                     # 逐个遍历数据
    print(item)