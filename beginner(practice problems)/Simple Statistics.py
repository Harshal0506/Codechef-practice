T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    A=list(map(int,input().split()))
    A.sort()
    S=sum(A[0+K:len(A)-K])
    print(S/(N-2*K))