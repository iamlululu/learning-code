import numpy as np

A = np.arange(2, 14).reshape((3, 4))
print(A, '\n')

print(np.argmax(A))                         # 输出最大值所在索引
print(A.argmax())

print(np.argmin(A))                         # 输出最小值所在索引
print(A.argmin())

print(np.mean(A))                           # 求平均值
print(A.mean())
print(np.average(A))

print(np.median(A))                         # 中位数

print(A)
print(np.cumsum(A))                         # 累加

print(A)
print(np.diff(A))                           # 累差

print(np.nonzero(A))                        # 判断非0,输出结果为了数组

print(np.sort(A))                           # 排序

print(A)
print(np.transpose(A))                      # 矩阵转置
print(A.transpose())
print(A.T)

print(A)                                    # 将矩阵中小于5的数等于5，大于9的数等于9，其余数值不变
print(np.clip(A, 5, 9))