T=int(input())
for _ in range(T):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    Count=0
    for i in a:
        if i%2==0:
            Count+=1
    if k==0 and Count==n:
        print("NO")
    else:
        if k<=Count:
            print("YES")
        else:
            print("NO")