# -*- coding: utf-8 -*-

'''
数据读取与合并
现有源自世界银行的四个数据集(编码均为UTF-8)：
1)economy-60-78.csv，
2)economy-79-19.csv，
3)population-60-78.csv，
4)population-79-19.csv，
其中分别存放了不同时间段（1960-1978和1979-2019）的
中国经济相关数据和中国人口及教育相关数据。
'''
#请将上述数据集内容读取至DataFrame结构中，
#年份为列索引，Indicator Name为行索引，
#观察其结构和内容，把它们合并为一个DataFrame。
#先按年份顺序沿着轴1拼接economy-60-78和economy-79-19；
#再按年份顺序沿着轴1拼接population-60-78和population-79-19；
#最后沿着轴0将前两次的拼接的结果拼接起来，命名为ChinaData
#输出ChinaData的形状
############begin############
import pandas as pd
from pandas import Series, DataFrame
eco1 = pd.read_csv('pandas_4/economy-60-78.csv',index_col='Indicator Name', encoding='utf-8')
eco2 = pd.read_csv('pandas_4/economy-79-19.csv',index_col='Indicator Name', encoding='utf-8')
pop1 = pd.read_csv('pandas_4/population-60-78.csv',index_col='Indicator Name', encoding='utf-8')
pop2 = pd.read_csv('pandas_4/population-79-19.csv',index_col='Indicator Name', encoding='utf-8')
eco = pd.concat([eco1, eco2], axis=1, sort=True)
pop = pd.concat([pop1, pop2], axis=1, sort=True)
ChinaData = pd.concat([eco, pop], axis=0, sort=True)
print(ChinaData.shape)
#############end#############