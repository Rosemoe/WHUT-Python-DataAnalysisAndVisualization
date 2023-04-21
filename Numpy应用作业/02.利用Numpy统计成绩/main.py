import numpy as np
name,subject=input(),input()
with open('step2/成绩单数字.csv', 'r', encoding='utf-8') as file:
    header = file.readline().strip().split(',')
    chart = [it.strip().split(',') for it in file.readlines()]
    names, array = [it[0] for it in chart],np.array([it[2:] for it in chart], dtype=np.int64)
    idx1, idx2 = names.index(name), header.index(subject) - 2
    print('{}同学的总分为{:.2f}\n{}同学的平均分为{:.2f}'.format(name, array.sum(axis=1)[idx1], name, array.mean(axis=1)[idx1]))
    print('{}课程平均成绩为{:.2f}\n{}课程中位数为{:.2f}\n{}课程标准差为{:.2f}'.format(subject, array.mean(axis=0)[idx2], subject, np.median(array, axis=0)[idx2], subject, np.std(array, axis=0)[idx2]))