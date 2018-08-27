n=raw_input()
k=n[::-1]
k=int(k)
while(k>0):
	c=k%10
	if((c%2)!=0):
		print c,
	k=k//10	
