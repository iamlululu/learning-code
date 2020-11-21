import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=6)
S = pd.DataFrame(np.arange(24).reshape((6, 4)), columns=['A', 'B', 'C', 'D'], index=dates)
print(S, '\n\n')

S.iloc[2, 2] = 111                                                      # 数据赋值
S.loc['20200101', 'B'] = 222
print(S)

S.A[S.A > 4] = 0                                                        # 数据赋值
# S[S.A > 4] =0
S['F'] = np.nan
S['G'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200101', periods=6))
print(S)