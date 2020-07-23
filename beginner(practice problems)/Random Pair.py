T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    M=max(A)
    P=A.count(M)
    Total=N*(N-1)/2
    if A.count(M)==1:
        A.remove(M)
        M=max(A)
        P=A.count(M)
        Choice=P


    else:
        Choice=P*(P-1)/2

    print(Choice/Total)


