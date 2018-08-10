x0,y0=map(int,input().split())
x1,y1=map(int,input().split())
z0=(x0*60)+y0
p0=(y1*60)+y1
p1=x0-p0
z1=p1//60
p1%=60
print(z1,p1,sep=" ")
