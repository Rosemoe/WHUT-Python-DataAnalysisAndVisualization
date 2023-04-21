a,b,s=int(input()),int(input()),input()
if s == '男':
    print("{}".format(int((a+b)*1.08/2)))
elif s == '女':
    print("{}".format(int((a*0.923+b)/2)))
else:
    print("无对应公式")