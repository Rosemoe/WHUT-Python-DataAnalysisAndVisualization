import pandas as pd
data = pd.read_csv('pandas_10/tips.csv')
op = input()
if op == 'gender':
    res = data.groupby(data['gender']).mean()
    print('男性顾客平均小费为：{:.2f}'.format(res.loc['Male', 'tip']))
    print('女性顾客平均小费为：{:.2f}'.format(res.loc['Female', 'tip']))
elif op == 'day':
    res = data.groupby(data['day']).agg({'tip': 'mean'})
    res.sort_values(by='tip', inplace=True)
    for k in res.index:
        print('{}：{:.2f}'.format(k, res.loc[k, 'tip']))
elif op == 'time':
    gp = data.groupby(data['time'])
    res = gp.agg({'tip': 'mean', 'total_bill': ['mean', 'sum']})
    print('午餐时间共{}条记录，共消费{:.2f}，平均每单消费{:.2f}，平均小费{:.2f}'.format(data.loc[data['time'] == 'Lunch'].shape[0], res.loc['Lunch', 'total_bill']['sum'], res.loc['Lunch', 'total_bill']['mean'], res.loc['Lunch', 'tip']['mean']))
    print('晚餐时间共{}条记录，共消费{:.2f}，平均每单消费{:.2f}，平均小费{:.2f}'.format(data.loc[data['time'] == 'Dinner'].shape[0], res.loc['Dinner', 'total_bill']['sum'], res.loc['Dinner', 'total_bill']['mean'], res.loc['Dinner', 'tip']['mean']))
elif op == 'smoker':
    gender = input()
    indices = data[(data['smoker'] == 'Yes') & (data['gender'] == gender) & (data['total_bill'] > 30)].index
    data['total_bill'] = data['total_bill'].apply(lambda x:f'{x:.2f}')
    data['tip'] = data['tip'].apply(lambda x:f'{x:.2f}')
    for i in indices:
        print(list(data.loc[i]))
elif op == 'average':
    avg = data['total_bill'] / data['size']
    n = int(input())
    avg.sort_values(ascending=False, inplace=True)
    data['total_bill'] = data['total_bill'].apply(lambda x:f'{x:.2f}')
    data['tip'] = data['tip'].apply(lambda x:f'{x:.2f}')
    for i in avg.head(n).index:
        print(list(data.loc[i]))
else:
    print('无数据')