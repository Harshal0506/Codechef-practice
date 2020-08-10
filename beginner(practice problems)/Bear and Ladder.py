Q=int(input())
for _ in range(Q):
    a,b=list(map(int,input().split()))
    if abs(a-b)==2 or (abs(a-b)==1 and min([a,b])%2==1):
        print("YES")
    else:
        print("NO")
        