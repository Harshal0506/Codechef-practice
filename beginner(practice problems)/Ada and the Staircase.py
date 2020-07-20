# cook your dish here
T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    H=list(map(int,input().split()))
    H.insert(0,0)
    Total=0
    for i in range(1,N+1):
        diff=H[i]-H[i-1]
        if diff>K:
            if diff%K==0:
                Total+= (diff//K -1)
            else:
                Total+=diff//K
    print(Total)
            