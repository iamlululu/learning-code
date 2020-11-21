import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a, b)
print('\n', a - b,'\n',  a + b)         # 数组加减
print(a * b)                            # 数组对应数据相乘
print(b ** 3)                           # 数组对应数据三次方

c = np.sin(a)                           # 三角函数
d = np.cos(b)
e = np.tan(a)
print('\n',c,'\n', d, '\n',e)
print(a < 38)                           # 判断数组的数据情况


a1 = np.array([[1, 1],
               [0, 1]])
b1 = np.arange(4).reshape((2, 2))
print(a1,'\n', b1)

c1 = a1 * b1                            # 对应位置数据相乘
c_dot = np.dot(a1, b1)                  # 矩阵乘法
c_dot1 = a1.dot(b1)
print(c1, '\n', c_dot,'\n', c_dot1)


a2 = np.random.random((2,4))            # 创建一个2*4阶随机矩阵
print(a2)
print(np.sum(a2))                       # 矩阵数据相加
print(np.max(a2))                       # 矩阵最大值
print(np.min(a2))                       # 矩阵最小值
print(np.sum(a2, axis = 1))             # 矩阵每一行相加
print(np.max(a2, axis = 0))             # 矩阵每一列中最大值
print(np.min(a2,axis = 1))              # 矩阵每一行中最小值
