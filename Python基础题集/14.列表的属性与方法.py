n,l=int(input()),[]
for i in range(n):
    args = input().split()
    if args[0] == 'print':
        print(l)
    else:
        cmd = 'l.' + args[0] + '('
        for i in range(1, len(args)):
            if i > 1:
                cmd=cmd+','
            cmd=cmd+args[i]
        eval(cmd+')')