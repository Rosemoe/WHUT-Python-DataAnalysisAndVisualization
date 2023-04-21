for i in range(1, 101):
    if len(str(i ** 3)) == 4 and len(str(i ** 4)) == 6:
        p = list(str(i ** 3)) + list(str(i ** 4))
        if len(set(p)) == 10:
            print(i)
            break