for i in range(1, 21):
    for j in range(1, int((100 - 5 * i) / 3) + 1):
        if (100 - 5 * i - 3 * j) > 0 and (i + j + (100 - 5 * i - 3 * j) * 3) == 100:
            print(i, j, (100 - 5 * i - 3 * j) * 3)