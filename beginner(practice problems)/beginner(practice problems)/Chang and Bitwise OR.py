T=int(input())
for _ in range(T):
    N=int(input())
    ans=0
    A=list(map(int,input().split()))
    for i in A:
        ans=ans | i
    print(ans)