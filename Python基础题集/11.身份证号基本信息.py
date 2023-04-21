s=input()
if (ord(s[16]) - ord('0')) % 2 == 0:
    p='女'
else:
    p='男'
print('出生：{}年{}月{}日\n性别：{}'.format(s[6:10], s[10:12], s[12:14], p))