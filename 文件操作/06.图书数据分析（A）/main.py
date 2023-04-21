q=input()
with open('step6/CBOOK.csv', 'r', encoding='utf-8') as file:
    chart = [it.strip().split(',') for it in file.readlines()[1:]]
    if q=='record':
        print(len(chart))
    elif q=='rank':
        idx=input()
        f=[it for it in chart if it[0] == idx]
        print('\n'.join(f[0]))
    elif q=='maxcomment':
        chart.sort(key=lambda x:int(x[5].replace('条评论', '')), reverse=True)
        for i in range(10):
            print('{} {}'.format(chart[i][1], chart[i][5]))
    elif q=='maxname':
        cnt=int(input())
        chart.sort(key=lambda x:len(x[1]), reverse=True)
        for i in range(cnt):
            print(chart[i][1])
    else:
        print('无数据')