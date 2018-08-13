a=input()
q=0
w=0
new=[]
list=[int(x) for x in input().split()]
z=len(list)
while(q==0):
    l=list[q]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        print(l,end=" ")
        new.insert(w,l)
        w+=1
    elif((list==new)and(l not in new)and(z==len(new))):
        print('unique')
    if(list==[]):
        break
