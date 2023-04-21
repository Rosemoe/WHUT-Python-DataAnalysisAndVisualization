n,p1,p2,r=int(input()),1,2,1.0
for i in range(1, n):
    if i % 2 != 0:
        r = r - i / p2
    else:
        r = r + i / p2
    p1,p2=p2,p1+p2
print('{:.6f}'.format(r))