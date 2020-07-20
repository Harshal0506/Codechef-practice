T=int(input())
for _ in range(T):
    n=int(input())
    disc1=0
    disc2=0
    disc3=0
    
    for _ in range(n):
        c,l,x=list(map(int,input().split()))
        if l==1:
            if disc1<x:
                disc1=x
                c1=c
            elif disc1==x and c<c1:
                c1=c
        elif l==2:
            if disc2<x:
                disc2=x
                c2=c
            elif disc2==x and c<c2:
                c2=c
        else:
            if disc3<x:
                disc3=x
                c3=c
            elif disc3==x and c<c3:
                c3=c
    print(disc1,c1)
    print(disc2,c2)
    print(disc3,c3)
