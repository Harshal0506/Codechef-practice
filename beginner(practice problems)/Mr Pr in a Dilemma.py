T=int(input())
for _ in range(T):
    a,b,c,d=list(map(int,input().split()))
    diff=abs(a-b)
    if abs(c-d)==0 and a==b:
        print("YES")
    elif abs(c-d)==0:
        print('NO')
    elif abs(a-b)%abs(c-d)==0:
        print('YES')
    else:
        print('NO')