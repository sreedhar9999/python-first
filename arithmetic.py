n,a,d=map(int,raw_input().split())
t=0
for i in range(0,n+1):
	t=t+(a+(i-1)*d)
print t
