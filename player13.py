b=int(input())
sum=0
while(int(b)>=1):
	d=int(b)%10
	sum=sum+(d**2)
	b=int(b)//10
	if(b==0):
		print(sum)
