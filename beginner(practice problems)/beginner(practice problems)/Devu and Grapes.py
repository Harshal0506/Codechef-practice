T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    Operations=0
    for i in (list(map(int,input().split()))):
        if i<K:
            Operations+=K-i
        else:
            m=i%K
            if m!=0:
                Operations+=min([m,K-m])
    print(Operations)