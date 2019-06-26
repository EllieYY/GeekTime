# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:06:54 2016

@author: SumaiWong
"""

import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy import dot
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize

from scipy.optimize import curve_fit


# # 自定义函数 e指数形式
# def func(x, a, b, c):
#     return a * np.sqrt(x) * (b * np.square(x) + c)

# iris = pd.read_csv('point.csv')
# x = iris['speed']
# y = iris['power']

# df = pd.DataFrame({'speed': x, 'power': y})
# sns.jointplot(x="speed", y="power", data=df, kind='scatter')
# plt.show()

# # 用3次多项式拟合
# f1 = np.polyfit(x, y, 2)
# print('f1 is :\n', f1)
#
# p1 = np.poly1d(f1)
# print('p1 is :\n', p1)
#
# #也可使用yvals=np.polyval(f1, x)
# yvals = p1(x)
# print('yvals is :\n',yvals)
# #绘图
# plot1 = plt.plot(x, y, 's',label='original values')
# plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4) #指定legend的位置右下角
# plt.title('polyfitting')
# plt.show()

# #非线性最小二乘法拟合
# popt, pcov = curve_fit(func, x, y)
# #获取popt里面是拟合系数
# print(popt)
# a = popt[0]
# b = popt[1]
# c = popt[2]
# yvals = func(x,a,b,c) #拟合y值
# print('popt:', popt)
# print('系数a:', a)
# print('系数b:', b)
# print('系数c:', c)
# print('系数pcov:', pcov)
# print('系数yvals:', yvals)
# #绘图
# plot1 = plt.plot(x, y, 's',label='original values')
# plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc=4) #指定legend的位置右下角
# plt.title('curve_fit')
# plt.show()


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15], dtype=float)
y = np.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59,
	                 84.47, 98.36, 112.25, 126.14, 140.03])

# 一个输入序列，4个未知参数，2个分段函数
def piecewise_linear(x, x0, y0, k1, k2):
	# x<x0 ⇒ lambda x: k1*x + y0 - k1*x0
	# x>=x0 ⇒ lambda x: k2*x + y0 - k2*x0
    return np.piecewise(x, [x < x0, x >= x0], [lambda x:k1*x + y0-k1*x0,
                                   lambda x:k2*x + y0-k2*x0])

# 用已有的 (x, y) 去拟合 piecewise_linear 分段函数
p , e = optimize.curve_fit(piecewise_linear, x, y)

xd = np.linspace(0, 10, 30)
plt.plot(x, y, "o")
plt.plot(xd, piecewise_linear(xd, *p))


# # 拟合线性模型： Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width
#
# # 正规方程法
# temp = iris.iloc[:, 1:4]
# temp['x0'] = 1
# X = temp.iloc[:, [3, 0, 1, 2]]
# Y = iris.iloc[:, 0]
# Y = Y.reshape(len(iris), 1)
# theta_n = dot(dot(inv(dot(X.T, X)), X.T), Y)  # theta = (X'X)^(-1)X'Y
# print
# theta_n
#
# # 批量梯度下降法
# theta_g = np.array([1., 1., 1., 1.])  # 初始化theta
# theta_g = theta_g.reshape(4, 1)
# alpha = 0.1
# temp = theta_g
# X0 = X.iloc[:, 0].reshape(150, 1)
# X1 = X.iloc[:, 1].reshape(150, 1)
# X2 = X.iloc[:, 2].reshape(150, 1)
# X3 = X.iloc[:, 3].reshape(150, 1)
# J = pd.Series(np.arange(800, dtype=float))
# for i in range(800):
#     # theta j := theta j + alpha*(yi - h(xi))*xi
#     temp[0] = theta_g[0] + alpha * np.sum((Y - dot(X, theta_g)) * X0) / 150.
#     temp[1] = theta_g[1] + alpha * np.sum((Y - dot(X, theta_g)) * X1) / 150.
#     temp[2] = theta_g[2] + alpha * np.sum((Y - dot(X, theta_g)) * X2) / 150.
#     temp[3] = theta_g[3] + alpha * np.sum((Y - dot(X, theta_g)) * X3) / 150.
#     J[i] = 0.5 * np.sum((Y - dot(X, theta_g)) ** 2)  # 计算损失函数值
#     theta_g = temp  # 更新theta
#
# print(theta_g)
# print(J.plot(ylim=[0, 50]))