P=int(input())
N=int(input())
i=float(input())
print('利息={:.2f}'.format(P*((1 + i) ** N) - P))