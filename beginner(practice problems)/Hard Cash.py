T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    A=list(map(int,input().split()))
    Total=0
    for i in A:
        Total+=i%K
    print(Total%K)