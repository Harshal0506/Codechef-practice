T=int(input())
for _ in range(T):
    N=int(input())
    for i in range(N):
        X,Y=list(map(int,input().split()))
    Total=1
    for i in range(2,N+1):
        Total^=i
    print(Total)