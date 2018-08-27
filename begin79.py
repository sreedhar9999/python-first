a,b=map(int,raw_input().split())
for i in range(1,max(a,b)+1):
	if(((a*b)/i==i) or(0 in (a,b))):
		print('yes')
		break
else:
	print('no')
