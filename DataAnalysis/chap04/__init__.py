import numpy as np

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 0-x轴， 1-y轴
print('===amin===')
print(np.amin(b))
print(np.amin(b, 0))
print(np.amin(b, 1))

print('===amax===')
print(np.amax(b))
print(np.amax(b, 0))
print(np.amax(b, 1))

# 最大值和最小值之差
print('===ptp===')
print(np.ptp(b))
print(np.ptp(b, 0))
print(np.ptp(b, 1))

# 百分位数
print('===percentile===')
print(np.percentile(b, 60))
print(np.percentile(b, 60, 0))
print(np.percentile(b, 60, 1))

# 中位数
print('===median===')
print(np.median(b))
print(np.median(b, 0))
print(np.median(b, 1))

#平均数
print('===mean===')
print(np.mean(b))
print(np.mean(b, 0))
print(np.mean(b, 1))

# 加权平均数
print('===average===')
print(np.average(a))
wts = np.array([1,2,3])
print(np.average(a, weights=wts))

# 方差、标准差
print('===std&var===')
print(np.std(a))
print(np.var(a))


# 排序
print('===sort===')
a1 = np.array([[4,3,2], [2,4,1]])
print(np.sort(a1))
print(np.sort(a1, axis=None))
print(np.sort(a1, axis=0))
print(np.sort(a1, axis=1))

print('===dtype===')
personType = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']})
peoples = np.array(
    [("Ellie", 27, 89, 92, 100), ("Kevin", 31, 87, 96, 99), ("li", 28, 82, 89, 91)],
    dtype=personType)
ages = peoples[:]['age']
names = peoples[:]['name']
print(np.mean(ages))

print('===arange&linespace===')
x1 = np.arange(1, 10, 2)
x2 = np.linspace(1, 9, 5)

print(x1)
print(x2)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
