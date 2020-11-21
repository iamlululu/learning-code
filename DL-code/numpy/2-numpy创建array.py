import numpy as np

a1 = np.array([[1, 2, 3],
               [4, 5, 6]])                      # 列表数组化

a2 = np.array([[1, 2, 3],
               [4, 5, 6]], dtype=int)           # dtype为设定数据类型

a3 = np.array([[1, 2, 3],
               [4, 5, 6]], dtype=float)         # dtype为设定数据类型

a4 = np.zeros((3, 4), dtype=int)                # 3*4阶零数组

a5 = np.ones((5, 4), dtype=int)                 # 5*4阶全1数组

a6 = np.empty((2, 3))                           # 数据接近为零的数组

a7 = np.arange(10, 20 ,2)                       # 从10到20，步长为2的数组

a8 = np.arange(12).reshape((3, 4))              # 从0到12，步长为1的，形状为3*4的数组

a9 = np.linspace(1, 10, 6).reshape((2, 3))      # 从1到10的范围平均隔断生成6个数据的数组

print(a9)