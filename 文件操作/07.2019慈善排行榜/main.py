q=input()
import re
with open('step7/2019Charity.csv', 'r', encoding='utf-8') as file:
    chart = [it.strip().split(',') for it in file.readlines()[1:]]
    if q.lower()=='total':
        sum=0
        for item in chart:
            sum += int(item[5])
        print('Total:{}万元'.format(sum))
    elif re.fullmatch('[0-9]+', q):
        f=[it for it in chart if it[0] == q]
        for x in f:
            print(' '.join(x))
        if len(f) == 0:
            print('No Record')
    else:
        f=[it[0:4] for it in chart if it[3]==q]
        if len(f) == 0:
            print('No Record')
        for x in f:
            print(' '.join(x))