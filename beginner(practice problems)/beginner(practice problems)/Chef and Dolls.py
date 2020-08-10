from collections import Counter
T=int(input())
for _ in range(T):
    N=int(input())
    A=Counter([])
    for i in range(N):
        A.update(list(map(int,input().split())))
    for i in A:
        if A[i]%2==1:
            print(i)
            break