T=int(input())
for _ in range(T):
    S=input()
    if len(S)%2==1:
        print("NO")
        continue
    All=set(S)
    for i in All:
        if S.count(i)==len(S)/2:
            print("YES")
            break
    else:
        print("NO")

