T=int(input())
for _ in range(T):
    N,S=list(map(int,input().split()))
    P=list(map(int,input().split()))
    C=list(map(int,input().split()))
    Budget=100-S
    minF=101
    minD=101
    for i in range(len(C)):
        if C[i]==0:
            if minD>P[i]:
                minD=P[i]
        else:
            if minF>P[i]:
                minF=P[i]
    if minD+minF>Budget:
        print("no")
    else:
        print("yes")
