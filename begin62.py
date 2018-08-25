c=raw_input()
n=list(c)
for i in range(0,len(n)):
	if((n[i]!='0') and (n[i]!='1')):
		print("no")
		break
else:
	print("yes")
	
