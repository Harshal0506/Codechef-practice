T=int(input())
for _ in range(T):
    Final=""
    N,K=list(map(int,input().split()))
    for i in list(map(int,input().split())):
        if i%K==0:
            Final+="1"
        else:
            Final+="0"
    print(Final)