n1=int(input())
n2=[int(a) for a in input().split()]
for b in range(n1):
    print(n2[b],b,sep=' ',end="\n")

