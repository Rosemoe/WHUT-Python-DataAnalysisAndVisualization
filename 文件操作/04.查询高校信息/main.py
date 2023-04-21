query=input()
with open('step4/university.csv', 'r', encoding='utf-8') as file:
    chart = [it.strip() for it in file.readlines()]
    q = [it for it in chart if it.split(',')[1] == query]
    print(chart[0])
    print(q[0], end='')