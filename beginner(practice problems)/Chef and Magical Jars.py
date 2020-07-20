T=int(input())
for _ in range(T):
    input()
    Min_dishes=0
    L=list(map(int,input().split()))

    for x in L:
        Min_dishes+=(x-1)
    Min_dishes+=1
    print(Min_dishes)
