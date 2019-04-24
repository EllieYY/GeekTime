import numpy as np
import pandas as pd
from pandas import DataFrame

data = DataFrame(pd.read_csv('data.csv'))
print(data)
newData = data.melt(id_vars=['A1', 'B1'], value_vars=['C1', 'D1', 'E1'])
print(newData)