T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    minimum=110
    maximum=0
    minL=0
    maxL=0
    for i in range(N):
        if A[i]<minimum:
            minimum=A[i]
            minL=i
        if A[i]>maximum:
            maximum=A[i]
            maxL=i
    if minL<maxL:
        print(minimum,maximum)
    else:
        print(maximum,minimum)



