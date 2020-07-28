T=int(input())
for _ in range(T):
    L=[]
    N,M=list(map(int,input().split()))
    for j in range(N):
        L.append(list(map(int,list(input()))))
    Total=0
    for i in range(M):
        sum=0
        for j in range(N):
            sum+=L[j][i]
        if sum>1:
            Total+=(sum*(sum-1))//2
    print(Total)


