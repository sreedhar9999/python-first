giv=input()
c=0
q=0
new=[]
list=[int(x) for x in input().split()]
while(c==0):
    l=list[c]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        new.insert(q,l)
        q+=1
    elif(l not in new):
        print(l)
    else:
        c=0
    if(list==[]):
        break
