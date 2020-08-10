T=int(input())
for _ in range(T):
    N,X,S=list(map(int,input().split()))
    
    for i in range(S):
        First,Second=list(map(int,input().split()))
        if X==First:
            X=Second
        elif X==Second:
            X=First
            
    print(X)
            
            