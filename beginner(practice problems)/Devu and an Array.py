N,Q=list(map(int,input().split()))
A=list(map(int,input().split()))
A.sort()
for _ in range(Q):
    t=int(input())
    if t<=A[-1] and t>=A[0]:
        print("Yes")
    else:
        print("No")