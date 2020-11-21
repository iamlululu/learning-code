import pandas as pd


left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(left, '\n', right)

res = pd.merge(left, right, on='key')                                           # merge合并
print(res)


left1 = pd.DataFrame({'key1': ['k0', 'k0', 'k1', 'k2'], 'key2': ['k0', 'k1', 'k0', 'k1'],
                      'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})
right1 = pd.DataFrame({'key1': ['k0', 'k1', 'k1', 'k2'], 'key2': ['k0', 'k0', 'k0', 'k0'],
                       'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']})
print(left1, '\n', right1)
print(pd.merge(left1, right1, on=['key1', 'key2']))                            # inner内部合并，只合并相同部分
# how=['inner', 'outer', 'left', 'right']
print(pd.merge(left1, right1, on=['key1', 'key2'], how='outer'))
print(pd.merge(left1, right1, on=['key1', 'key2'], how='outer', indicator=True), '\n')
print(pd.merge(left1, right1, on=['key1', 'key2'], how='outer', indicator='indicator_colunm'))


boy = pd.DataFrame({'k': ['k0', 'k1', 'k2'], 'age': [1, 2, 3]})
girl = pd.DataFrame({'k': ['k0', 'k0', 'k3'], 'age': [4, 5, 6]})
mer = pd.merge(boy, girl, on='k', suffixes=['_boy', '_girl'], how='outer')
print(mer)