import pandas as pd
import numpy as np

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 
                              'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                              'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
print(lowercased)

print(lowercased.map(meat_to_animal))

data['animal'] = lowercased.map(meat_to_animal)
print(data)

print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

data = pd.Series([1., -999., 2., -999., -1000., 3.])

print(data.replace(-999, np.nan))#(被替换值，替换值)
data.replace([-999, -1000], np.nan)
print(data.replace([-999, -1000], [np.nan,0]))#分别传入列表，将多个值替换为多个值
data.replace({-999: np.nan, -1000: 0})#传入字典，键被值替换

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

transform = lambda x: x[:4].upper()
print(data.index.map(transform))
# data.index = data.index.map(transform)#修改原始数据
print(data)

index_to_now_index = {'Ohio': 'OHIO', 'Colorado': 'COLO', 'New York': 'NEW'}
data.index = data.index.map(index_to_now_index)
print(data)

print(data.rename(index=str.title, columns=str.upper))#title()首字母大写，upper()全部大写
data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'},inplace=True)
print(data)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)#(18,25] (25,35] (35,60] (60,100]
print(cats)
print("-----------------------------------------------")

print(cats.codes)
print("-----------------------------------------------")
print(cats.categories)

print(pd.value_counts(cats))#每个bin有几个数据
print("-----------------------------------------------")

print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))#right=False，左闭右开   
print("-----------------------------------------------")

grouped_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=grouped_names))

data = np.arange(1,21)
print(data)

print(pd.cut(data, 4))

print(pd.cut(data, 4, precision=2))#保留两位小数

data = [1,1,2,3,4,5,5,8,9]#更具样本分位数进行划分
cats = pd.qcut(data, 2)
print(cats)

data = np.random.randn(1000)
cats = pd.qcut(data, 4)
print(cats)

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col)>3])

print(data[np.abs(data)>8])
print(np.sign(data)*8)
data[np.abs(data)>8] = np.sign(data)*8
print(data)

array = np.arange(-2,18).reshape((4,5))
data = pd.DataFrame(array)
print(data)
print(np.sign(data))

print(data[(np.abs(data)>3)].any())

data[np.abs(data)>3] = np.sign(data)*3
print(data.describe())

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
print(df)
print(pd.get_dummies(df['key'],prefix='key'))

print(df[['data1']])

dummies = pd.get_dummies(df['key'], prefix='key')

df_with_dummies = df[['key']].join(dummies)
print(df_with_dummies)

movies = pd.read_csv('数据变换\movies.csv',sep=',')
print(movies.head())

all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
print(genres)

zero_martrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_martrix, columns=genres)
print(dummies)

gen = movies.genres[0]
gen.split('|')
dummies.columns.get_indexer(gen.split('|'))

for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))   
print(movies_windic.head(2))

np.random.seed(12345)
values = np.random.rand(10)
print(values)

bins = [0,0.2,0.4,0.6,0.8,1]
print(pd.get_dummies(pd.cut(values, bins)))

data = pd.Series(np.random.randn(9),index=[['a','a','a','b','b','c','c','d','d'],[1,2,3,1,3,1,2,2,3]])
print(data)
print(data.index)#Multiindex————多层索引

#通过外层索引选取
print(data['b'])
print(data['b':'c'])
print(data.loc[['b','c']])

print(data[:,2])#所有内层索引为二的行

print(data.unstack())#将内层索引的唯一值转换为列索引

print(data.unstack().stack())#stack()将列索引转换为内层索引

frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index=[['a','a','b','b'],[1,2,1,2]],
                      columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
print(frame)

frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
print(frame)

print(frame['Ohio'])
print(frame['Ohio','Green'])

MultiIN = pd.MultiIndex.from_arrays([['Ohio','Ohio','Colorado'],['Green','Red','Green']],
                                   names=['state','color'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=MultiIN)
print(frame2)

frame.swaplevel('key1','key2')#交换索引，默认交换行索引

print(frame.swaplevel('state','color',axis=1))

frame.sort_index(level=1)#对索引排序,默认行索引

frame.sort_index(level=1,axis=1)#列索引

print(frame.swaplevel(0,1).sort_index(level=0))

print(frame)
# frame.sum(level='key2')
# frame.sum(level='color',axis=1)

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],\
                       'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)

frame2 = frame.set_index(['c','d'])
print(frame2)
print(frame.set_index(['c','d'],drop=False))

#Groupby机制
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),'data2': np.random.randn(5)})
print(df)

grouped = df[['data1']].groupby(df['key1'])
print(grouped)

print(grouped.mean())

mean = df['data1'].groupby([df['key1'],df['key2']]).mean()
print(mean)

print(mean.unstack())

states = np.array(['Ohio','California','New York','Ohio','Ohio'])
years = np.array([2005,2005,2006,2005,2006])
print(df['data1'].groupby([states,years]).mean())

numeric_columns = df.select_dtypes(include=[np.number]).columns
print(df.groupby('key1')[numeric_columns].mean())

print(df.groupby('key1').size())#统计每个分组的元素个数