import pandas as pd
import numpy as np
                                                                                # 合并pandas数据
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
print(df1, '\n', df2, '\n', df3)

result = pd.concat([df1, df2, df3], axis=0, ignore_index=True)                  # contat()方法合并
print(result)


df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
print(df4,  '\n', df5)
print(pd.concat([df4, df5]))
print(pd.concat([df4, df5], join='inner', ignore_index=True))

# result1 = pd.concat([df4, df5], axis=1, join_axes=[df4.index])
# print(result1)

result3 =df1.append([df2, df3], ignore_index=True)
print(result3)