T=int(input())
for _ in range(T):
    Count=0
    N=int(input())
    L=list(map(int,input().split()))
    G=list(map(int,input().split()))
    for i in range(N):
        if G[i]-L[i]<0:
            break
    else:
        Count+=1
    G.reverse()
    for i in range(N):
        if G[i]-L[i]<0:
            break
    else:
        Count+=2

    if Count==0:
        print("none")
    elif Count==1:
        print("front")
    elif Count==2:
        print("back")
    else:
        print("both")
