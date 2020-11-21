import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

print(df.dropna(axis=0,how='any'))                               # 去除缺失数据，how = {'any', 'all'}
print(df.dropna(axis=0,how='all'))

print(df.fillna(value=666))                                      # 填充缺失数据

print(df.isnull())                                               # 判断是否缺失数据
print(np.any(df.isnull()) == True)