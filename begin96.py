n,a,d=map(int,raw_input().split())
s=0
for i in range(0,n+1):
	s=s+(a+(i-1)*d)
print s
