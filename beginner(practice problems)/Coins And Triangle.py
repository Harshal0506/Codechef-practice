T=int(input())
for _ in range(T):
    N=int(input())
    Height=0
    t=1
    x=0
    while(N>=x+t):
        x+=t
        t+=1
        Height+=1
    print(Height)

