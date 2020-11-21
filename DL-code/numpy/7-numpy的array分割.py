import numpy as np

A = np.arange(12).reshape((3, 4))
print(A)

print(np.split(A, 2, axis=1))                              # 对矩阵进行分割
print(np.split(A, 3, axis=0))
print(np.vsplit(A, 3))
print(np.hsplit(A ,2))

print(np.array_split(A, 3, axis=1))                        # 不等量分割