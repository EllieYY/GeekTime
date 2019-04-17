import matplotlib.pyplot as plt
import seaborn as sns

# 数据准备
data = sns.load_dataset('car_crashes')
print(data.head(10))

sns.pairplot(data)
# plt.show()

# 用 seaborn 画散点图
sns.jointplot(x='total', y='speeding', data=data, kind='scatter')

# 用 seaborn 画核密度图
sns.jointplot(x='total', y='speeding', data=data, kind='kde')

# 用 seaborn 画 Hexbin 图
sns.jointplot(x='total', y='speeding', data=data, kind='hex')
plt.show()