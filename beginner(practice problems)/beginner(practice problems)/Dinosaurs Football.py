T=int(input())
for _ in range(T):
    N,k=list(map(int,input().split()))
    L=[]
    for i in range(N-k,N+1):
        L.append(i)
    for i in range(1,N-k):
        L.append(i)
    for i in L:
        print(i,end=" ")
    print()