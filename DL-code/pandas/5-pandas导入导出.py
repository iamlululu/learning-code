import pandas as pd


input_file = 'Z:/learning code/Machine Learning code/pandas/视觉中国爬取.html'            # 导入数据
data = pd.read_html(input_file)
print(data)

pd.to_pickle(data,'Z:/learning code/Machine Learning code/pandas/视觉中国爬取.pickle')    # 导出数据
