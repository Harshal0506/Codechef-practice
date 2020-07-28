T=int(input())
for _ in range(T):
    N,X=list(map(int,input().split()))
    min=max=x=0
    S=list(input())
    for i in S:
        if i=="L":
            x-=1

            if x<min:
                min=x
        if i=='R':
            x+=1
            if x>max:
                max=x
    print(max-min+1)
