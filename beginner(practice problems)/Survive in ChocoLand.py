import math

T = int(input())
for _ in range(T):
    N, K, S = list(map(int, input().split()))
    Visit = math.ceil(K * S / N)
    maxOpenDay = S - S // 7
    if maxOpenDay >= Visit:
        print(Visit)
    else:
        print(-1)
