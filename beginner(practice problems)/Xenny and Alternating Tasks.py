T=int(input())
for _ in range(T):
    N=int(input())
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    case1=sum(X[::2])+sum(Y[1::2])
    case2=sum(X[1::2])+sum(Y[::2])
    print(min([case1,case2]))