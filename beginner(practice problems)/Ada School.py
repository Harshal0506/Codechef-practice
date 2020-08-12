T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    if N%2==1 and M%2==1:
        print("NO")
    else:
        print("YES")