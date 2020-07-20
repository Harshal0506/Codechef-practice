T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    sum=0
    money=0
    while(sum<=K and N>0):
        T,D=list(map(int,input().split()))
        sum+=T
        N-=1
    if sum>K:
        money=(sum-K)*D
    while(N>0):
        T,D=list(map(int,input().split()))
        money+=T*D
        N-=1
    print(money)

    
    
