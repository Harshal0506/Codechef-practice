# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    P=list(map(int,input().split()))
    P.sort()
    Profit=0
    for i in range(N):
        A=P[-1]-i
        if A>0:
            Profit+=A
        P.pop()
    print(Profit%1000000007)
    
        