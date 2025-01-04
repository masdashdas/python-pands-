# Python数据处理学习笔记

这个代码仓库包含了我学习Python数据处理过程中的代码笔记,主要使用pandas和numpy库进行数据操作。

## 目录结构

### 1. 数据清洗
- 字符串操作 - 包含字符串处理、正则表达式、pandas矢量化字符串函数等
- 处理缺失值 - None/NaN的处理、删除和填充缺失值、去除重复数据等

### 2. 数据变换
- 数据映射和替换
- 离散化和分箱
- 处理异常值
- 哑变量处理
- 多层索引操作

### 3. 数据集成
- 数据合并(merge)
- 连接操作(join) 
- 轴向连接(concat)
- 处理重叠数据

### 4. 数据规约
- 随机采样
- 数据抽样方法

### 5. 实战案例
- 中国篮球运动员基本信息预处理

## 主要功能

- 数据清洗和预处理
- 数据转换和规约
- 数据集成和合并
- 处理缺失值和异常值
- 字符串和文本处理
- 数据采样

## 依赖库
```python
pandas
numpy
```

## 使用说明

每个.py文件都包含了详细的代码示例和注释说明。建议按照以下顺序学习:

1. 先学习基础的数据清洗操作
2. 然后是数据变换的各种方法
3. 接着学习数据集成的不同方式
4. 最后是数据规约方法

## 代码示例

### 数据清洗示例
```python
# 处理缺失值
import pandas as pd
import numpy as np

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
# 删除缺失值
cleaned = data.dropna()
# 填充缺失值
filled = data.fillna(0)
```

### 数据变换示例
```python
# 数据映射
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow'
}
data['animal'] = data['food'].map(meat_to_animal)
```

## 注意事项

- 代码中大量使用了pandas和numpy的函数
- 部分示例需要特定的数据文件支持
- 建议先掌握pandas基础知识再学习这些代码

## 参考资料

- Python数据分析相关书籍
- pandas官方文档
- numpy官方文档

## 贡献

欢迎提出建议和改进意见!

## 许可证

MIT License
