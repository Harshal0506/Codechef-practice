T=int(input())
for _ in range(T):
    N,Q=list(map(int,input().split()))
    prev=0
    total=0
    for _ in range(Q):
        P=list(map(int,input().split()))
        total+= abs(prev-P[0])
        total+=abs(P[0]-P[1])
        prev=P[1]
    print(total)

