import pandas as pd
from pandas import DataFrame


data = DataFrame(pd.read_csv('data.csv'))
print('=== before ===')
print(data)


print('=== after ===')
data['food'] = data['food'].str.lower()
data.drop_duplicates("food", inplace=True) # 删除重复行
data['ounces'].fillna(data['ounces'].mean(), inplace=True)
data['ounces'] = data['ounces'].apply(lambda a: abs(a)) # 负值不合法，取绝对值
print(data)