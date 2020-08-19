import math
T=int(input())
for _ in range(T):
    N=int(input())
    for i in range(math.floor((N)**0.5),0,-1):
        if N%i==0:
            print(N//i-i)
            break
        