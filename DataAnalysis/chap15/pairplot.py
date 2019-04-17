import matplotlib.pyplot as plt
import seaborn as sns
# 数据准备
iris = sns.load_dataset('iris')
print(iris.head(10))

# 用 Seaborn 画成对关系
sns.pairplot(iris)
plt.show()
