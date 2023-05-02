import pandas as pd
import numpy as np

'''
返回df中最大值与最小值的差
'''
def sub(df):
    ######## Begin #######
    return df.max() - df.min()
    ######## End #######

'''
利用groupby、agg、统计函数和自定义函数sub，求每个大洲红酒消耗量的最大值与最小值的差以及啤酒消耗量的和
'''
def main():
    ######## Begin #######
    data = pd.read_csv('pandas_7/drinks.csv')
    print(data.groupby('continent').agg({'wine_servings': sub, 'beer_servings': np.sum}))
    ######## End #######

if __name__ == '__main__':
    main()