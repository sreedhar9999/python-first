a,b=map(int,input().split())
c=min(a,b)
if((a%c)==0 and (b%c)==0):
	print(c)
else:
	while(c>1):
		c-=1
		if((a%c)==0 and(b%c)==0):
			print(c)
			break
