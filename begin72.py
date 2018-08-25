s=raw_input()
l=list(s)
p=['a','e','i','o','u']
for i in range(0,len(l)):
	if(l[i] in p):
		print ('yes')
		break
else:
	print('no')
