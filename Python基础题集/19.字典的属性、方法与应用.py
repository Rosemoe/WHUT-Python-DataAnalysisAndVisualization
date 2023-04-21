n,l,nm,nb=int(input()),{},input().split(','),input().split(',')
for i in range(len(nm)):
    l[nm[i]] = nb[i]
for i in range(n):
    args = input().split()
    if args[0] == 'print':
        print(l)
    elif args[0] == 'add':
        l[args[1]] = args[2]
    elif args[0] == 'del':
        if args[1] in l.keys():
            del l[args[1]]
        else:
            print('键不存在')
    elif args[0] == 'update':
        l[args[1]] = args[2]
    elif args[0] == 'value':
        print(list(l.values()))
    elif args[0] == 'key':
        print(list(l.keys()))
    elif args[0] == 'clear':
        l.clear()