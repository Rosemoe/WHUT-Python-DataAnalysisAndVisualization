import numpy as np
arr = np.genfromtxt('step4/China Minsheng Bank.csv', names=True, delimiter=',', encoding='utf-8', dtype=None)
op = input()
if op == '最高价':
    n = int(input())
    arr.sort(axis=0,order='最高价')
    print('最高价从高到低前{}名:'.format(n))
    for i in range(n):
        print('{} {}元'.format(arr[-i-1]['日期'],arr[-i-1]['最高价']))
elif op == '开盘价':
    n = int(input())
    print('开盘价从低到高前{}名:'.format(n))
    arr.sort(axis=0,order='开盘价')
    for i in range(n):
        print('{} {}元'.format(arr[i]['日期'],arr[i]['开盘价']))
elif op == '成交金额':
    n = int(input())
    arr.sort(axis=0,order='成交金额')
    arr = [x[-1] for x in arr[-n:]]
    print('成交金额最多的{}天成交额为{}元'.format(n,sum(arr)))
elif op == '日期':
    d = input()
    pos = np.argwhere(arr['日期']==d)
    for i in pos:
        print(' '.join([str(x) for x in list(arr[i][0])]))