import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=6)
S = pd.DataFrame(np.arange(24).reshape((6, 4)), columns=['A', 'B','C', 'D'],index=dates)
print(S, '\n\n')

print(S['A'],'\n',  S.A)                                                    # 数据的选择
print(S[0:3], '\n\n', S['20200101':'20200103'])

print(S.loc['20200102'])                                                    # select by label:loc
print(S.loc[:,['A','B']])
print(S.loc['20200102',['A','B']])

print(S.iloc[3])                                                            # select by position:iloc
print(S.iloc[3, 2])
print(S.iloc[3:5, 1:3])
print(S.iloc[[1, 3, 5], 1:3])

# print(S.ix[:3, ['A', 'C']])                                                .ix因选取边缘数据不严谨被弃用

print(S)                                                                    # Boolean indexing
print(S[S.A > 8])