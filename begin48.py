n=int(raw_input())
l=[int(x) for x in raw_input().split()]
c=0
for i in range(0,n):
	c=c+l[i]
print c/n	
