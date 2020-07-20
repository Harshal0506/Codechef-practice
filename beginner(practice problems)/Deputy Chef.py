# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    D=list(map(int,input().split()))
    strength=[]
    final=[]
    
    A.insert(0,A[-1])
    A.append(A[1])
    
    
    for i in range(1,N+1):
        strength.append(A[i-1]+A[i+1])
    for i in range(N):
        if D[i]>strength[i]:
            final.append(D[i])
    if len(final)>0:
        print(max(final))
    else:
        print(-1)
            
            
            
        