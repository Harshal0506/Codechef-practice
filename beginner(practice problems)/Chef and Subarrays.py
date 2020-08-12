import numpy
T=int(input())
for _ in range(T):
    T=0
    N=int(input())
    A=list(map(int,input().split()))
    for i in range(1,N+1):
        for j in range(0,N-i+1):
            L=A[j:j+i]
            if sum(L)==numpy.prod(L):
                T+=1
    print(T)
                

