p,t=map(int,input().split())
u=[int(x) for x in input().split()]
s=sorted(u)
print(s[p-t])
