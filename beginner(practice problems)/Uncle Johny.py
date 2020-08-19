T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    K=int(input())-1
    required=A[K]
    A.sort()
    print(A.index(required)+1)