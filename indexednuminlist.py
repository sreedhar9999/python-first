giv=int(raw_input())
new=[]
list=[int(x) for x in raw_input().split()]
for i in range(0,giv):
	if(i==list[i]):
		new.append(i)
	elif((new==[]) and (i==(giv-1))):
		print('-1')
s=sorted(new)
c=len(s)
for i in range(0,c):
	print s[i],
