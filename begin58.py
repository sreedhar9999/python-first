n,k=map(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
for i in range(0,n):
	if(l[i]==k):
		print('yes') 
		break
else:
	print('no')
