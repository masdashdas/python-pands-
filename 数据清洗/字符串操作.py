import pandas as pd
import numpy as np

val = 'a,b,  guido'
print(val.split(','))#拆分

piececs = [x.strip() for x in val.split(',')]#去除空格
print(piececs)

first, second, third = piececs
print(first + '::' + second + '::' + third)

print('::'.join(piececs))#以'::'为分隔符连接,传入序列数据

print('guido' in val)   #判断是否包含某字符串

print(val.index('guido'))#返回子串首字母的位置

print(val.find(':'))#不会报错，返回-1表示不存在
#index(':')不存在会报错

print(val.count(','))#返回出现的次数

print(val)

print(val.replace(',', '::'))#替换字符串

print(val.replace(',', ''))#替换为空字符串

#正则表达式
import re

text = "foo bar\t baz \tqux"
print(re.split('\s+',text))

regex = re.compile('\s+')#先编译可以重复使用
print(regex.split(text))

print(regex.findall(text))#返回所有符合正则表达式的子串

#match 和 search 
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'''[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'''
regex = re.compile(pattern, re.IGNORECASE)#忽略大小写(re.IGNORECASE)
print(regex.findall(text))

m = regex.search(text)
#<re.Match object; span=(5, 20), match='dave@google.com'>
print(m)

print(text[m.start():m.end()])#索引截取

print(regex.match(text))#匹配开头

print(regex.sub('REDACTED', text))#替换

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+\.[A-Z]{2,4})'
regex = re.compile(pattern, re.IGNORECASE)

m = regex.match('wesm@right.net')
print(m.group())
print(regex.findall(text))#返回元组列表

print(regex.sub(r'Username:\1,Domian:\2',text))

#pandas的矢量化字符串函数
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = pd.Series(data)
print(data)

print(data.isnull())

print(data.str.contains('gmail'))#判断是否包含gmail

print(data.str.findall(pattern,flags=re.IGNORECASE))

matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)

print(data.str.get(0))#不能切片
print(data.str[:5])

