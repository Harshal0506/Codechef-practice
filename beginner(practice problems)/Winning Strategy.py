t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    x,y=0,0
    x+=a[0]
    if  n>=2:
        y+=a[1]
    for i in range(2,n,2):
        y+=a[i]
        if i+1<n:
            x+=a[i+1]
    if x==y:
        print('draw')
    elif x>y:
        print("first")
    else:
        print('second')