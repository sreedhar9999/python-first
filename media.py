# your code goes here
n1=int(input())
n2=[int(b) for b in input().split()]
p=sorted(n2)
if n1%2==0:
    a=((n1)-1)//2
    b=x+1
    c=(p[a]+p[b])/2
    print(c)
else:
    a=(n1)//2
    print(p[a])
