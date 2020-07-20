# cook your dish here
T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    Data=list(map(int,input().split()))
    Non1=N-Data.count(1)
    if Non1>K:
        print("NO")
    else:
        print("YES")