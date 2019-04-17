from sklearn import preprocessing
import numpy as np

# 初始化数据 行-样本 列-特征
x = np.array([[ 0., -3.,  1.],
              [ 3.,  1.,  2.],
              [ 0.,  1., -1.]])

# Min-Max规范化
print('=== Min-Max规范化 ===')
min_max_scaler = preprocessing.MinMaxScaler()
min_max_x = min_max_scaler.fit_transform(x)
print(min_max_x)

# Z-Score规范化
print('=== Z-Score规范化 ===')
z_scaled_x = preprocessing.scale(x)
print(z_scaled_x)

# 小数定标规范化
print('=== 小数定标规范化 ===')
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)


y = np.array([[5000.], [16000.], [58000.]])
print(min_max_scaler.fit_transform(y))