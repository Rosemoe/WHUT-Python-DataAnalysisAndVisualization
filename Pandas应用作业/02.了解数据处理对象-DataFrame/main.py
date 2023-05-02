# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def create_dataframe():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    dictionary = {'states':['0hio','0hio','0hio','Nevada','Nevada'],
             'years':[2000,2001,2002,2001,2002],
             'pops':[1.5,1.7,3.6,2.4,2.9]}
    df1=DataFrame(dictionary,index=['one','two','three','four','five'])
    df1['new_add']=[7,4,5,8,2]
    # ********** End **********#

    #返回df1
    return df1