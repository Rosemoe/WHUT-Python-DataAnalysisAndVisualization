n=input()
with open('step5/admit2.csv', 'r') as file:
    header = [it.strip() for it in file.readline().split(',')]
    content = [it.split(',') for it in file.readlines()]
    chart = [dict([(header[i], it[i]) for i in range(len(it))]) for it in content]
    if n == 'Research':
        k1,a1,k2,a2 = 0,0,0,0
        for data in chart:
            if float(data['Chance of Admit']) >= 0.9:
                a1 += 1
                k1 += int(data['Research'])
            elif float(data['Chance of Admit']) <= 0.7:
                a2 += 1
                k2 += int(data['Research'])
        print('Research in >=90%:{:.2f}%\nResearch in <=70%:{:.2f}%'.format(k1/a1*100, k2/a2*100))
    elif n == '1':
        filtered = [it for it in chart if float(it['Chance of Admit']) >= 0.8]
        filtered2 = [it for it in filtered if float(it['University Rating']) >= 4]
        print('Top University in >=80%:{:.2f}%'.format(len(filtered2)/len(filtered)*100))
    elif n == '2':
        filtered = [float(it['TOEFL Score']) for it in chart if float(it['Chance of Admit']) >= 0.8]
        mx,mn,sum=-114514,114514,0
        for data in filtered:
            mx = max(mx, data)
            mn = min(mn, data)
            sum += data
        print('TOEFL Average Score:{:.2f}\nTOEFL Max Score:{:.2f}\nTOEFL Min Score:{:.2f}'.format(sum/len(filtered), mx, mn))
    elif n == '3':
        filtered = [float(it['CGPA']) for it in chart if float(it['Chance of Admit']) >= 0.8]
        mx,mn,sum=-114514,114514,0
        for data in filtered:
            mx = max(mx, data)
            mn = min(mn, data)
            sum += data
        print('CGPA Average Score:{:.3f}\nCGPA Max Score:{:.3f}\nCGPA Min Score:{:.3f}'.format(sum/len(filtered), mx, mn))
    else:
        print('ERROR')