from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from sklearn.tree import DecisionTreeRegressor

boston = load_boston()

features = boston.data
prices = boston.target

train_features, test_features, train_price, test_price = train_test_split(features, prices, test_size=0.33)

dtr = DecisionTreeRegressor()
dtr.fit(train_features, train_price)

predict_price = dtr.predict(test_features)

print('二乘偏差均值：', mean_squared_error(test_price, predict_price))
print('绝对值偏差均值：', mean_absolute_error(test_price, predict_price))