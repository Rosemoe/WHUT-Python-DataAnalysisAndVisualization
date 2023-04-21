mapping = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.5,
    'D': 1.3,
    'D-': 1.0,
    'F': 0
}
g,t1,t2 = input(),0,0
while g != '-1':
    k=float(input())
    t1+=mapping[g]*k
    t2+=k
    g=input()
print('{:.2f}'.format(t1/t2))