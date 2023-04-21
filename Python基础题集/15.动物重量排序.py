s=input()
l=[]
while s!='':
    l1=s.split()
    w = l1[1]
    if 'kg' in w:
        l1.append(float(w[:-2]))
    else:
        l1.append(float(w[:-1]) * 1000)
    l.append(l1)
    s=input()
l.sort(key=lambda p:p[2])
print([s[0:2] for s in l])