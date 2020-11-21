import numpy as np

A = np.arange(4)
print(A)

B = A
C = A
D =B
print(B,C,D)

A[0] = 11                                   # A,B,C,D会进行关联，改变A的值会同步改变B,C,D的值
print(A,B,C,D)
D[0] = 44
print(A,B,C,D)

E = A.copy()                                # deep copy,不将A和E进行关联,只将数据进行拷贝
print(A)
A[1:3] = [22, 33]
print(A, E)