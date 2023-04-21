limits = [0, 3000, 12000, 25000, 35000, 55000, 80000]
decrement = [0, 210, 1410, 2660, 4410, 7160, 15160]
rate = [3, 10, 20, 25, 30, 35, 45]
num = float(input())
if num < 0:
    print('error')
else:
    n = num - 5000
    m = 0
    for i in range(len(limits)):
        limit = limits[i]
        if n > limit:
            m = n * rate[i] / 100 - decrement[i]
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(m, num - m))