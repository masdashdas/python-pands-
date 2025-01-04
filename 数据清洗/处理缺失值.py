import pandas as pd
import numpy as np
from numpy import nan as NA

#None为python中的空值
#nan 为nupy中的空值
#NAN 为pandas中的空值

#两种缺失值都能被检测
string_data = pd.Series(['aardvark', 'artichoke',np.nan, 'avocado'])
print(string_data)

print(string_data.isnull())

string_data[0] = None
print(string_data.isnull())

data = pd.Series([1, NA, 3.5, NA, 7])
print(data)

print(data.dropna())#删除缺失值,返回新的对象

print(data.notna())
print(data[data.notnull()])

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                      [NA, NA, NA], [NA, 6.5, 3.]]) 

print(data)

cleaned = data.dropna()
print(cleaned)

print(data.dropna(how='all'))#how='all'丢弃全为nan的行

print(data.dropna(axis=1, how='all'))#丢弃全为nan的列

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)

print(df.dropna(thresh=2))

print(df.fillna(0))

print(df.fillna({1:0.5, 2:0}))

_=df.fillna(0,inplace=True)
print(df)

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)

print(df.fillna(method='ffill'))#前一个非nan值填充 

print(df.fillna(method='ffill', limit=2))#限制向前两步填充

data = pd.Series([1., NA, 3.5, NA, 7])  
print(df.fillna(data.mean()))#均值填充

#移除重复数据 

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

print(data.duplicated())#判断是否重复,返回Series

print(data.drop_duplicates())#返回去重后的数据

data['v1'] = range(7)
print(data.drop_duplicates(['k1']))#比较指定列,返回去重后的数据

print(data.drop_duplicates(['k1', 'k2'], keep='last'))#丢弃前一个重复值,保留最后出现的

