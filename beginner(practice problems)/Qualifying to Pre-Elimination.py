T=int(input())
for _ in range(T):
    N,k=list(map(int,input().split()))
    S=list(map(int,input().split()))
    Total=k
    S.sort(reverse=True)
    value=S[k-1]
    for i in range(k,len(S)):
        if S[i]!=value:
            break
        Total+=1
    print(Total)