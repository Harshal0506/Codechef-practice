from collections import Counter
T=int(input())
for _ in range(T):
    N,Q=list(map(int,input().split()))
    S=Counter(input())
    for i in range(Q):
        C=int(input())
        pending=0
        for j in S.values():
            if j>C:
                pending+=j-C
        print(pending)
        
        