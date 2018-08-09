# your code goes here
N=int(input())
if N<=100000:
	y=[int(x) for x in raw_input().split()]
	y.sort()
	print" ".join(map(str,y))
