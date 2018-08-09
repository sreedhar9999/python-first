n,a,d=map(int,raw_input().split())
x=0
for i in range(0,n+1):
	x=x+(a+(i-1)*d)
print x
