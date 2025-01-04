import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['a', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)

print(pd.merge(df1, df2, on='key'))

print(pd.merge(df1, df2))# 默认on以相同列名的列为key

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                     'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))#列名不同的情况

print(pd.merge(df1, df2, how='outer'))#外连接

print(pd.merge(df1, df2, how='left'))#左连接

print(pd.merge(df1, df2, how='right'))#右连接

print(pd.merge(df1, df2, how='inner'))#内连接

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                      'key2': ['one', 'two', 'one'],
                      'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                       'key2': ['one', 'one', 'one', 'two'],
                       'lval': [4, 5, 6, 7]})

print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))#列索相同时默认前一个后缀为_x，后一个后缀_y
print(left)
print(right)

print(pd.merge(left, right, on='key1',suffixes=('_left', '_right')))#列索引相同时，指定后缀

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                       'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])    

print(left1)
print(right1)
print(pd.merge(left1, right1, left_on='key', right_index=True))
print(pd.merge(left1, right1, left_on='key', right_index=True,how='outer'))

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
rigth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
print(lefth)
print(rigth)

print(pd.merge(lefth, rigth, left_on=['key1', 'key2'], right_index=True))
print(pd.merge(lefth, rigth, left_on=['key1', 'key2'], right_index=True,how='outer'))

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                       index=['a', 'c', 'e'],
                       columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14.]],
                        index=['b', 'c', 'd', 'e'],
                        columns=['Missouri', 'Alabama'])
print(left2)
print(right2)
print(pd.merge(left2, right2, left_index=True, right_index=True))
print(pd.merge(left2, right2, left_index=True, right_index=True,how='outer'))

print(left2.join(right2,how='outer'))#默认按索引合并,不能有重叠的列
print(left1.join(right1,on='key'))

#轴向连接
arr = np.arange(12).reshape((3, 4))
print(arr)
print(arr.shape)

print(np.concatenate([arr, arr]))
print(np.concatenate([arr, arr]).shape)
print(np.concatenate([arr, arr], axis=1))
print(np.concatenate([arr, arr], axis=1).shape)

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(s1)
print(s2)
print(s3)
print(pd.concat([s1, s2, s3]))
print(pd.concat([s1, s2, s3],axis=1))

s4 = pd.concat([s1, s3])
print(s4)

print(pd.concat([s1, s4], axis=1))

print(pd.concat([s1, s4], axis=1,join='inner'))

#层次化索引
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)

print(result.unstack())

print(pd.concat([s1, s2,s3], axis=1,keys=['one', 'two', 'three']))

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))

print(pd.concat({'level1': df1, 'level2': df2},axis=1))

print(pd.concat({'level1': df1, 'level2': df2},axis=1,names=['upper', 'lower']))

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print(df1)
print(df2)
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], ignore_index=True))# 重新排序索引(合并后行索引没有实际意义)

#合并重叠数据
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],index=['f','e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),index=['f','e', 'd', 'c', 'b', 'a'])
print(a)
b[-1] = np.nan
print(b)
print(np.where(pd.isnull(a),b,a))
print(b[:-2].combine_first(a[2:]))
print(a[2:].combine_first(b[:-2]))

