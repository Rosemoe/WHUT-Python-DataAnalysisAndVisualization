a,n=int(input()),int(input())
if 1<=a and a<=9 and n>=0:
    r = 0
    for i in range(1, n+1):
        r += int(str(a) * i)
    print(r)
else:
    print('data error')