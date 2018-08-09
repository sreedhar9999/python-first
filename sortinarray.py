# your code goes here
N=int(input())
if N<=100000:
	S=[int(x) for x in raw_input().split()]
	S.sort()
	print" ".join(map(str,S))
