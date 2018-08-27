n=input()
l=list(n)
if((len(l)%2)!=0):
    l[len(l)//2]='*'
    for i in range(0,len(l)):
        print(l[i],end='')
else:
    l[(len(l)%2)]='*'
    l[(len(l)//2)-1]='*'
    for i in range(0,len(l)):
        print(l[i],end='')
