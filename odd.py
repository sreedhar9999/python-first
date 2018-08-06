low,high=map(int,raw_input().split())

for i in range (low+1,high+1):
	if(i%2)!=0:
		print i,
