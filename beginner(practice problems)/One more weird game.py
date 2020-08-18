T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    print(N*(M-1)+M*(N-1))