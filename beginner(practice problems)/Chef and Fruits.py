T=int(input())
for _ in range(T):
    N,M,K=list(map(int,input().split()))
    x=abs(N-M)-K
    if x<0:
        print(0)
    else:
        print(x)