T=int(input())
for _ in range(T):
    prev=-7
    i=int(input())
    Q=list(map(int,input().split()))
    for p in range(i):
        if Q[p] == 1:
            if p-prev<6:
                print("NO")
                break
            prev=p
    else:
        print("YES")



