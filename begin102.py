a=int(raw_input())
if((a%2)!=0):
	print(a)
else:
	while((a%2)==0):
		a=a/2
		if((a%2)!=0):
			print(int(a))
		break	
