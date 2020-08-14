T=int(input())
for _ in range(T):
    X1,X2,X3,V1,V2=list(map(int,input().split()))
    TC=abs(X1-X3)/V1
    TK=abs(X2-X3)/V2
    if TC==TK:
        print("Draw")
    elif TC>TK:
        print("Kefa")
    else:
        print("Chef")