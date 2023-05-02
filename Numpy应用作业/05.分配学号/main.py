import numpy as np
str_types = lambda x:np.dtype([(v, np.str_, 16) for v in x])
majors = np.genfromtxt('step5/MajorCode.csv', delimiter=',', encoding='utf-8', dtype=str_types(['major', 'code']))
schools = np.genfromtxt('step5/schoolCode.csv', delimiter=',', encoding='utf-8', dtype=str_types(['school', 'code']))
students = np.genfromtxt('step5/studentList.csv', delimiter=',', encoding='utf-8', dtype=str_types(['name', 'gender', 'school', 'major', 'class', 'year']))
name, cls = input(), input()
def alloc(inf):
    mj = str(majors[np.argwhere(majors['major'] == inf[0]['major'])][0]['code'][0])
    sc = str(schools[np.argwhere(schools['school'] == inf[0]['school'])][0]['code'][0])
    mates = students[np.argwhere(students['class'] == inf[0]['class'])]
    rank = int(np.argwhere(mates['name'] == inf[0]['name']).squeeze()[0]) + 1
    return '012' + str(inf[0]['year'][2:]) + sc + mj + str(inf[0]['class'][-4:]) + '{:02d}'.format(rank)
for i in students[np.argwhere(students['name'] == name)]:
    print(alloc(i), ' '.join(list(i[0])))
for i in students[np.argwhere(students['class'] == cls)]:
    print(alloc(i), ' '.join(list(i[0])))