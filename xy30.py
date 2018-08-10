s0,t0=map(int,input().split())
s1,t1=map(int,input().split())
c0=(s0*60)+t0
d0=(s1*60)+t1
d1=c0-d0
c1=d1//60
d1%=60
print(c1,d1,sep=" ")
