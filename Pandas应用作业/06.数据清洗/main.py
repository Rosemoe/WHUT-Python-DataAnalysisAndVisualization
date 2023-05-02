# -*- coding: utf-8 -*-
'''
数据清洗
'''
import pandas as pd
ChinaData = pd.read_csv('pandas_6/ChinaData.csv',index_col = 0, encoding='utf-8')
'''
请针对ChinaData完成如下操作。
'''
# 2.1 按如下格式输出删除前ChinaData的形状
# 格式：原表形状(x, y)
############begin############
print('原表形状{}'.format(ChinaData.shape))
line0 = ChinaData.shape[0]
#############end#############

# 2.2 直接删除ChinaData的空白行
# 提示：dropna,inplace
############begin############
ChinaData.dropna(inplace=True, how='all')
#############end#############

# 2.3 按如下格式输出删除后ChinaData的形状
# 格式：新表形状(x, y)
############begin############
print('新表形状{}'.format(ChinaData.shape))
line1 = ChinaData.shape[0]
#############end#############

# 2.4 按如下格式输出被删除的空行数
# 格式：XX个空白行被删除。
############begin############
print('{}个空白行被删除。'.format(line0-line1))
#############end#############

# 2.5 查找数据最完整（空值最少）的年份并输出
# 提示：notnull(),根据值找索引
############begin############
print(ChinaData.notnull().sum(axis=0).idxmax())
#############end#############

# 2.6 前向填充"男性吸烟率（吸烟男性占所有成年人比例）"，输出2000年至2019年的数据
# fillna,ffill
############begin############
ChinaData.loc['男性吸烟率（吸烟男性占所有成年人比例）'].fillna(method='ffill',inplace=True)
print(ChinaData.loc['男性吸烟率（吸烟男性占所有成年人比例）','2000':'2019'])
#############end#############
