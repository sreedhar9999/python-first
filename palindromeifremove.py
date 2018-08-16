giv=input()
t=giv
for i in range(97,123):
    giv=giv.replace(chr(i),'')
    if(giv==giv[::-1]):
        print('YES')
        break
    giv=t
    if(i==122):
        print('NO')
