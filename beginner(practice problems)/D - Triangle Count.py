# cook your dish here
T=int(input())
for i in range(1,T+1):
    L,K=list(map(int,input().split()))
    if L>=K:
        triangle=(L+1-K)*(L+2-K)//2
        print("Case {}: {}".format(i,triangle))
    else:
        print("Case {}: 0".format(i))