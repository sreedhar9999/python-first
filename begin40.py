n=int(raw_input())
f0=0
f1=1
f=1
for i in range(0,n):
	print f,
	f=f0+f1
	f0=f1
	f1=f
