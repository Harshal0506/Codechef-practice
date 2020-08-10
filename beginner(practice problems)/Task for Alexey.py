import math
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    mini=None
    for i in range(0,N-1):
        for j in range(i+1,N):
            if mini==None or mini>A[i]*A[j]/math.gcd(A[i],A[j]):
                mini=A[i]*A[j]/math.gcd(A[i],A[j])
    print(int(mini))