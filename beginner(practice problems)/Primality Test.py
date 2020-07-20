import math
T=int(input())
for _  in range(T):
    N=int(input())
    if N==1:
        print("no")
        continue
    for i in range(2,math.floor(N**0.5)+1):
        if N%i==0:
            print("no")
            break
    else:
        print("yes")