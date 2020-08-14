N,K=list(map(int,input().split()))
L=[0]*N
Count=0
for _ in range(K):
    inp=input().split()
    if len(inp)==1:
        Count=0
        L=[0]*N
        print(Count)
    else:
        index=int(inp[1])-1
        L[index]=(L[index]+1)%2
        if L[index]==1:
            Count+=1
        else:
            Count-=1
        print(Count)
        
    