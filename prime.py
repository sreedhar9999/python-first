N= int(raw_input())
 
for i in range(2, int(N/2)):
    if N % i  == 0:
        print("no")
        break
else:
    print("yes")
