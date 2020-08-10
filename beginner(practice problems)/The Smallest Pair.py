T=int(input())
for _ in range(T):
    N=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(a[0]+a[1])