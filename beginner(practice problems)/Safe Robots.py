# cook your dish here
T=int(input())
for _ in range(T):
    s=list(input())
    sa,sb=list(map(int,input().split()))
    A=s.index('A')
    B=s.index('B')
    while(A<=B):
        if A==B:
            print("unsafe")
            break
        A+=sa
        B-=sb
    else:
        print("safe")
    