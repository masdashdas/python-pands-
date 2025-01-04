import pandas as pd
import datetime

# 读取数据
file_one = pd.read_csv('中国篮球运动员基本信息预处理\运动员信息采集01.csv', encoding='GBK')
file_two = pd.read_excel('中国篮球运动员基本信息预处理\运动员信息采集02.xlsx')

# 合并数据
all_data = pd.merge(file_one, file_two, how='outer')  # 默认按照相同列名合并

# 过滤国籍为中国
all_data = all_data[all_data['国籍'] == '中国']

# 查找并删除重复行
print(all_data.info())
print(all_data[all_data.duplicated().values == True])  # 找出重复行，重行返回True
all_data = all_data.drop_duplicates(ignore_index=True)  # 去重后重新排序
print(all_data.head())

# 过滤项目为篮球
basketball_data = all_data[all_data['项目'] == '篮球']
basketball_data = basketball_data.copy()

# 处理出生日期
initial_date = datetime.datetime.strptime('1900-01-01', '%Y-%m-%d')
for idx, date in basketball_data['出生日期'].items():
    if isinstance(date, int):
        new_time = (initial_date + datetime.timedelta(days=date)).strftime('%Y-%m-%d')
        basketball_data.at[idx, '出生日期'] = new_time

# 提取年份
basketball_data['出生日期'] = basketball_data['出生日期'].apply(lambda x: x[:4])
print(basketball_data['出生日期'].head(10))

# 处理身高数据
def fill_height(data, gender):
    height_data = data['身高'].dropna()
    avg_height = height_data.apply(lambda x: float(x[:-2])).mean()  # 去掉单位“厘米”并计算平均值
    avg_height_str = f"{int(avg_height)}厘米"
    data['身高'] = data['身高'].fillna(avg_height_str)
    data['身高'] = data['身高'].apply(lambda x: int(x[:-2]))
    return data

# 分离男女数据
male_data = basketball_data[basketball_data['性别'] == '男']
male_data = male_data.copy()
male_data = fill_height(male_data, '男')

female_data = basketball_data[basketball_data['性别'] == '女']
female_data = female_data.copy()

# 替换女性身高中的非标准格式
height_replacements = {
    '191cm': '191厘米',
    '1米89公分': '189厘米',
    '2.01米': '201厘米',
    '187公分': '187厘米',
    '1.97M': '197厘米',
    '1.98米': '198厘米',
    '192cm': '192厘米'
}
female_data['身高'] = female_data['身高'].replace(height_replacements)

# 填充女性身高
female_data = fill_height(female_data, '女')

# 计算女运动员的平均体重，填充缺失值
female_weight = female_data['体重'].dropna()
female_weight = female_weight.apply(lambda x: float(x[:-2]))  # 确保转换为浮点数
fill_female_weight = round(female_weight.mean())
# 填充缺失值
female_data['体重'] = female_data['体重'].fillna(f"{fill_female_weight}公斤")
print(female_data)

basketball_data = pd.concat([male_data, female_data], ignore_index=True)
basketball_data['体重']=basketball_data['体重'].apply(lambda x:int((x[0:-2])))
basketball_data.rename(columns={'体重':'体重/kg'},inplace=True)
print('-----------------------------------------------------------------------------------')
print(basketball_data.head(5))
print('-----------------------------------------------------------------------------------')
smaple_data = basketball_data.sample(n=50,replace=True)
print(smaple_data[:100])

female_data.loc[:'体重']=female_data.loc[:'体重'].replace({'88千克':'88kg'})
print(female_data.loc[:'体重'])
female_data.loc[:'体重']=female_data.loc[:'体重'].replace({'76公斤':'76kg'})
print(female_data.loc[:'体重'])

print(all_data[all_data['省份']=='广东' ].head())
print(pd.get_dummies(all_data['项目']).head())

print(all_data.describe())

female_data = basketball_data[basketball_data['性别'].apply(lambda x: x == '女')]
print(female_data['身高'].groupby(female_data['省份']).mean().astype(int))
print(female_data['体重/kg'].groupby(female_data['省份']).mean().astype(int))

print(all_data.set_index('省份')[:5])
