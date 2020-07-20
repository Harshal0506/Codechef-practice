from collections import Counter
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    Repeated_max=Counter(A).most_common(1)[0][1]
    print(N-Repeated_max)
    
