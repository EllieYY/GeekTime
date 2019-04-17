import pandas as pd
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])

d = {'a':1, 'b':2, 'c':3, 'd':4}
x3 = Series(d)
print(x1)
print(x2)
print(x3)

data = {'语文': [66, 95, 93, 90,80],'英语': [65, 85, 92, 88, 90],'数学': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦'], columns=['英语', '数学', '语文'])
print(df1)

df2 = df2.drop(columns=['语文'])
df2 = df2.drop(index=['张飞'])
df2.rename(columns={'数学':'几何'}, inplace=True)
print(df2.describe())


pysqldf = lambda sql:sqldf(sql, globals())
sql = "select * from df1"
print(pysqldf(sql))


score = DataFrame(pd.read_excel('data.xlsx'))
score.to_excel('data1.xlsx')
# print(score)



