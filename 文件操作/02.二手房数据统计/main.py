n=input()
with open('step2/house.csv', 'r', encoding='utf-8') as file:
    header = file.readline().replace(',', ' ').strip()
    chart = [it.strip().split(',') for it in file.readlines()]
    if n == '最高总价':
        k=int(input())
        chart.sort(key=lambda x:float(x[8]), reverse=True)
        f = chart[0:min(len(chart), k)]
        print(header)
        for v in f:
            print(' '.join(v))
    elif n == '最大面积':
        k=int(input())
        chart.sort(key=lambda x:float(x[7]), reverse=True)
        f = chart[0:min(len(chart), k)]
        print(header)
        for v in f:
            print(' '.join(v))
    elif n == '最高单价':
        mx,idx = -1,-1
        for i in range(len(chart)):
            v = chart[i]
            w = float(float(v[8])/float(v[7]))
            if w > mx:
                mx,idx=w,i
        print(header)
        print(' '.join(chart[idx]))
    elif n == '精装电梯房单价':
        f = [it for it in chart if (it[5] == '精装' and it[6] == '有电梯')]
        m,p=0,0
        for v in f:
            m += float(v[7])
            p += float(v[8])
        print('{:.2f}万元'.format(p/m))
    elif n == '房屋朝向':
        t = input()
        f = [it for it in chart if it[3] == t]
        if len(f) == 0:
            print('无数据')
        else:
            print('{}套'.format(len(f)))
    else:
        f = [it for it in chart if n in it[1]]
        print(header)
        for v in f:
            print(' '.join(v))
        if len(f) == 0:
            print('未找到相关数据')
