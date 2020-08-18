T=int(input())
for _ in range(T):
    G=int(input())
    for i in range(G):
        I,N,Q=list(map(int,input().split()))
        if N%2==1:
            I=2 if I==1 else 1
            if I==Q:
                print(N//2+1)
            else:
                print(N//2)
        else:
            print(N//2)