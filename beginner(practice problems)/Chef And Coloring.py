from collections import Counter
T=int(input())
for _ in range(T):
    N=int(input())
    S=Counter(list(input())).most_common(1)[0][1]
    print(N-S)