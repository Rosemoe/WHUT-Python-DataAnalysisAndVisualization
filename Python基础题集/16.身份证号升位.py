s=input()
if int(s[6:8]) >= 5:
    s=s[0:6]+'19'+s[6:15]
else:
    s=s[0:6]+'20'+s[6:15]
w='7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2'.split()
checksum='1 0 X 9 8 7 6 5 4 3 2'.split()
sum=0
for i in range(17):
    sum+=int(w[i])*(ord(s[i]) - ord('0'))
s=s+checksum[sum%11]
print(s)