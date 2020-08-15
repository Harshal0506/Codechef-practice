from collections import defaultdict 
T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    L=defaultdict(lambda:[])
    for i in range(N):
        Day,Value=list(map(int,input().split()))
        L[Day].append(Value)
    max=-1
    for i in L:
        for j in L[i]:
            if max<j:
                max=j
                index=i
    
    del L[index]
    A=max
    max=-1
    for i in L:
        for j in L[i]:
            if max<j:
                max=j
    
    B=max
    print(A+B)