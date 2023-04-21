import numpy as np
import numpy.random as npr
op=input().lower()
if op == 'array':
    print(eval('np.array(' + input() + ')'))
elif op == 'arange':
    p1,p2,p3=map(int, input().split())
    print(np.arange(start=p1,stop=p2,step=p3))
elif op == 'linspace':
    p1,p2,p3=map(int, input().split())
    print(np.linspace(start=p1,stop=p2,num=p3))
elif op == 'logspace':
    p1,p2,p3,p4=map(int, input().split())
    print(np.array([p4]) ** np.linspace(start=p1,stop=p2,num=p3,endpoint=False))
elif op == 'zeros':
    p1,p2=map(int, input().split())
    print(np.zeros((p1,p2)))
elif op == 'ones':
    p1,p2=map(int, input().split())
    print(np.ones((p1,p2)))
elif op == 'full':
    p1,p2,p3=map(int, input().split())
    print(np.full((p1,p2),p3))
elif op == 'identity':
    print(np.identity(int(input())))
elif op == 'randint':
    p0,p1,p2,p3,p4=map(int, input().split())
    npr.seed(p0)
    print(npr.randint(low=p1,high=p2,size=(p3,p4)))
else:
    print('ERROR')