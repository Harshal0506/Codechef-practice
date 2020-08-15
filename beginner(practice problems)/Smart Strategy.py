import numpy as np
T=int(input())
for _ in range(T):
    N,a=list(map(int,input().split()))
    D=list(map(int,input().split()))
    Q=list(map(int,input().split()))
    Product=np.prod(D)
    
    for i in Q :
        print(i//Product,end=" ")
    print()