# cook your dish here
T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    S=sum(list(map(int,input().split())))
    if K==1:
        if S%2==0:
            print("odd")
        else:
            print("even")
    else:
        print("even")