T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    L=[]
    Total=0
    for i in range(1,N+1):
        if A[i-1]==0:
            L.insert(0,i)
        else:
            ind=L.index(A[i-1])
            L.insert(ind+1,i)
            Total+=min([len(L[:ind+1]),len(L[ind+2:])])
    print(Total)
    
            
            