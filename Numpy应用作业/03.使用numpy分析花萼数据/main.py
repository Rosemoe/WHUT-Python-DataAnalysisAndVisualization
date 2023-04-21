import numpy as np
data,n = np.unique(np.loadtxt('step3/iris_sepal_length.csv', dtype=np.float64)), int(input())
np.sort(data, axis=0, kind='stable')
data = data[0:min(n,data.shape[0])]
dic = {'最大值': np.max, '最小值':np.min,'均值':np.mean,'方差':np.var,'标准差':lambda x:np.std(x, ddof=1)}
for k,v in dic.items():
    print('花萼长度的{}是：{:.2f}'.format(k, v(data)))