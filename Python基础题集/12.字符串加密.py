s=list(input())
for i in range(len(s)):
    c = ord(s[i])
    if c >= ord('a') and c <= ord('z'):
        c += 3
        if c > ord('z'):
            c -= 26
    if c >= ord('A') and c <= ord('Z'):
        c += 5
        if c > ord('Z'):
            c -= 26
    s[i] = chr(c)
print(''.join(s))