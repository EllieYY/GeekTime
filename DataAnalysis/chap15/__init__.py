import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


N = 1000
x = np.random.randn(N)
y = np.random.randn(N)

# 用Matplotlib绘图
plt.scatter(x, y, marker='x')
plt.show()

# 用seaborn画散点图
df = pd.DataFrame({'time': x, 'power': y})
sns.jointplot(x="time", y="power", data=df, kind='scatter')
plt.show()