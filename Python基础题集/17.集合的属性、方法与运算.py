n=int(input())
s=set(input().split())
for i in range(n):
    args = input().split()
    if args[0]=='add':
        s.add(args[1])
    elif args[0]=='print':
        p=list(s)
        p.sort()
        print(p)
    elif args[0]=='del':
        if args[1] in s:
            s.remove(args[1])
    elif args[0]=='update':
        s.update(args[1:])
    elif args[0]=='clear':
        s.clear()