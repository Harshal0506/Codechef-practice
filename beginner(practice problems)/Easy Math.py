T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    Maxsum=0
    for i in range(0,N-1):
        for j in range(i+1,N):
            L=str(A[i]*A[j])
            L=list(L)
            L=list(map(int,L))
            Current=sum(L)
            if Maxsum<Current:
                Maxsum=Current
    print(Maxsum)
               
            
            