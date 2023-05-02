import pandas as pd
import numpy as np

def task3():
    #********** Begin **********#
    #读取三个csv文件
    abbrevs = pd.read_csv('pandas_9/state-abbrevs.csv')
    areas = pd.read_csv('pandas_9/state-areas.csv')
    pop = pd.read_csv('pandas_9/state-population.csv')
    # 合并pop和abbrevs并删除重复列
    merged = abbrevs.merge(pop, how='outer', left_on='abbreviation', right_on='state/region')
    merged.drop('abbreviation', axis=1, inplace=True)
    # 填充对应的全称
    merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
    merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
    # 合并面积数据
    merged = merged.merge(areas, on='state', how='left')
    # 删掉这些缺失值
    merged.dropna(inplace=True)
    # 取year为2010年的数据，并将索引设为state列
    merged2010 = merged[merged['year'] == 2010].copy()
    merged2010.set_index('state', inplace=True)
    # 计算人口密度
    merged2010['density'] = merged2010['population'] / merged2010['area (sq. mi)']
    # 对密度求和
    # 由于人口密度中分为成年人的人口密度和未成年人的人口密度，所以我们需要对两个值进行求合得到最终的人口密度；
    merged2010['density'] = merged2010['density'].groupby(merged2010['state/region']).transform(sum)
    # 对值进行排序
    sorted = merged2010.loc[merged2010['ages'] == 'total'].sort_values(by='density', ascending=False)['density']
    sorted.name = None
    # 输出人口密度前5名和倒数5名
    print('前5名：')
    print(sorted.head())
    print('后5名：')
    print(sorted.tail())
    #********** End **********#

