T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    Avg=sum(A)/N
    if Avg in A:
        print(A.index(Avg)+1)
    else:
        print("Impossible")