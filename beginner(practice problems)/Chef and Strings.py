T=int(input())
for _ in  range(T):
    N=int(input())
    A=list(map(int,input().split()))
    Total=0
    for i in range(1,N):
        Jump=A[i]-A[i-1]
        if Jump<0:
            Jump*=(-1)
        Total+=Jump-1
    print(Total)
        