T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    Girls=list(map(int,input().split()))
    Girls.insert(0,0)
    Sum_g=0
    for i in range(K):
        Sum_g+=Girls[i]
    Max=0
    for i in range(1,N-K+2):
        Sum_g-=Girls[i-1]
        Sum_g+=Girls[i+K-1]
        if Sum_g>Max:
            Max=Sum_g
    print(Max)
        
        