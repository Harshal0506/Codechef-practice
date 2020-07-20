T=int(input())
for _ in range(T):
    S=0
    L=input()
    H=list(map(int,input().split()))
    W=list(map(int,input().split()))
    H.sort()
    W.sort()
    for i in range(int(L)):
        S+=min([H[i],W[i]])
    print(S)
