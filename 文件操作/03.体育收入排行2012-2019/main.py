import re
n=input()
with open('step3/2012-19sport.csv', 'r', encoding='utf-8') as file:
    header = file.readline()
    chart = [it.strip().split(',') for it in file.readlines()]
    if n.lower()=='sport':
        n = input()
        if (not re.fullmatch('[0-9]+', n)) or int(n) < 2012 or int(n) > 2019:
            print('Wrong Input')
        else:
            f = [it for it in chart if it[-1] == n]
            types = []
            for t in f:
                if not (t[-2] in types):
                    types.append(t[-2])
            types.sort()
            for i in range(len(types)):
                print('{}: {}'.format(i + 1, types[i]))
            k = int(input()) - 1
            f = [it for it in f if it[-2] == types[k]]
            sum = 0
            for item in f:
                print(' | '.join(item)[1:])
                sum += float(re.search('([0-9]+(\.[0-9]+)?)', item[2]).group())
            print('TOTAL: ${:.2f} M'.format(sum))
    elif (not re.fullmatch('[0-9]+', n)) or int(n) < 2012 or int(n) > 2019:
        print('Wrong Input')
    else:
        k = int(input())
        f = [it for it in chart if it[-1] == n]
        f.sort(key=lambda x:int(re.search('[0-9]+', x[0]).group()))
        f = f[0:min(len(f), k)]
        for item in f:
            out = ' | '.join(item)
            if out.startswith('#'):
                print(out[1:])
            else:
                print(out)