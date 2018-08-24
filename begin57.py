n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
c=0
for i in range(0,n):
	if(l[i]==k):
		c+=1
		l[i]=' '
print c
