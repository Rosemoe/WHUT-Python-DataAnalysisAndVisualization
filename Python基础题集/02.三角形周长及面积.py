import math
a=float(input())
b=float(input())
c=float(input())
print('周长={:.2f}'.format(a+b+c))
s=(a+b+c)/2
print('面积={:.2f}'.format(math.sqrt(s*(s-a)*(s-b)*(s-c))))