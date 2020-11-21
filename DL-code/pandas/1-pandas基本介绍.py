import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])                                 # pandas基本介绍
print(s)

dates = pd.date_range('20200101',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b','c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

print(df.columns)                                       # df列名称
print(df.values)                                        # df数值

print(df.describe())                                    # 描述df

print(df.T)                                             # 转置df

print(df.T.sort_index(axis=1, ascending=False))         # 对列进行倒序排序

print(df.sort_values(by='c'))                           # 对数据列c的数据进行排序