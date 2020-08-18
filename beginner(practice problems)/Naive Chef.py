T=int(input())
for _ in range(T):
    N,A,B=list(map(int,input().split()))
    X=list(map(int,input().split()))
    Total=N*N
    Required=X.count(A)*X.count(B)
    print(Required/Total)