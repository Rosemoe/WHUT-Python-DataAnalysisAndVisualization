p1,p2,d,it,s1,s2=1,1,int(input()),0,0,0
while s1 + s2 < d:
    s1,s2 = s1 + p1, s2 + p2
    p1,p2,it = p1*2, p2/2, it+1
if s1+s2 > d:
    p1,p2=p1/2,p2*2
    s1,s2=s1-p1,s2-p2
    r=d-s1-s2
    s1,s2=s1+r*p1/(p1+p2),s2+r*p2/(p1+p2)
print('{}\n{} {}'.format(it, round(s2,1), round(s1,1)))