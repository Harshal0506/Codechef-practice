T=int(input())
for _ in range(T):
    N,K,E,M=list(map(int,input().split()))
    Result=[]
    for i in range(N-1):
        Result.append(sum(list(map(int,input().split()))))
    Current_chef=sum(list(map(int,input().split())))
    Result.sort()
    Needed=Result[N-K-1]+1-Current_chef
    if Needed>M:
        print("Impossible")
    elif Needed<0:
        print(0)
    
    else:
        print(Needed)