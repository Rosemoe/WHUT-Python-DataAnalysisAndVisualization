cnt,n,num=0,int(input()),2
while cnt<n:
    flag = 1
    s=str(num)
    l=len(s)
    for i in range(l // 2):
        if s[i] != s[l-1-i]:
            flag = 0
            break
    if flag:
        for i in range(2, int(num ** 0.5) + 2):
            if num % i == 0 and num != i:
                flag = 0
                break
    if flag:
        print(num, end=' ')
        cnt = cnt + 1
    num=num+1