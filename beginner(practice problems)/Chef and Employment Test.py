T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    A=list(map(int,input().split()))
    A.sort()
    print(A[(N+K)//2])