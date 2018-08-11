N=int(input())
if N<=100000:
	z=[int(x) for x in raw_input().split()]
	z.sort()
	print" ".join(map(str,z))
