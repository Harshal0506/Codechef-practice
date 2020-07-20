# cook your dish here
T=int(input())
for _ in range(T):
    A=dict()
    N,M=list(map(int,input().split()))
    F=list(map(int,input().split()))
    P=list(map(int,input().split()))
    
    for i in range(N):
        A[F[i]]=A.get(F[i],0)+P[i]
    print(min(A.values()))