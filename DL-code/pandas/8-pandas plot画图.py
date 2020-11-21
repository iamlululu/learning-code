import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data1 = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = np.cumsum(data)
data1 = data1.cumsum()
print(data1.head(5))
data.plot()
data1.plot()
ax = data1.plot.scatter(x='A', y='B', color='DarkBlue',label='Class 1')
data1.plot.scatter(x='A', y='C', color='DarkGreen',label='Class 2', ax=ax)
plt.show()