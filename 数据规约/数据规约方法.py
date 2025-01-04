import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(5*4).reshape(5,4))
print(df)

sampler = np.random.permutation(5)# 随机打乱行索引
print(sampler)

print(df.take(sampler))# take方法打乱排序
print(df.sample(n=3))#随机选取3行

choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)#replace=True可以重复取
print(draws)

