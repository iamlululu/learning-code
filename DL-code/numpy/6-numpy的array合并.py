import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B))                                   # 数组垂直合并 vertical stack
D = np.hstack((A, B))                                   # 数组水平合并 horizontal stack
print(C, '\n\n', D, '\n')
print(A.shape,'\n',  C.shape, '\n', D.shape, '\n')

print(A[np.newaxis, :], '\n')                           # 一维向量矩阵化，矩阵后可转置
print(A[:, np.newaxis], '\n')



A = np.array([1, 1, 1])[np.newaxis, :]
B = np.array([2, 2, 2])[np.newaxis, :]
print(A, '\n\n', B, '\n')

E = np.concatenate((A, B, B, A), axis = 0)            # 多个矩阵进行合并，参数axis决定合并方向
F = np.concatenate((A, B, B, A), axis = 1)
print(E, '\n\n', F)