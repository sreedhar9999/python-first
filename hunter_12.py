num=int(input())
list=[int(x) for x in input().split()]
for i in range(0,num):
        sum1=0
        sum2=0
        for x in range(0,i):
                sum1=sum1+list[x]
        for y in range(i+1,num):
                sum2=sum2+list[y]
        if(sum1==sum2):
                print('yes')
                break
        elif(i==(num-1)):
                print('no')
