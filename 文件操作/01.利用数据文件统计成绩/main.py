n=int(input())
with open('step1/成绩单.csv', 'r', encoding='utf-8') as file:
    chart = [it.strip().split(',') for it in file.readlines()]
    chart.sort(key=lambda x:int(x[9]))
    print('最低分{}分,最高分{}分'.format(chart[0][9], chart[-1][9]))
    print(chart[0:min(n,len(chart))])
    print(chart[max(0, len(chart) - n):])
    p = [0 for i in range(6)]
    for i in range(3, 9):
        for item in chart:
            p[i - 3] += int(item[i])
    p = [float('{:.2f}'.format(k / len(chart))) for k in p]
    print(p)