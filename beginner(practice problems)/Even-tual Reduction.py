T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    for i in set(S):
        if S.count(i)%2!=0:
            print("NO")
            break
    else:
        print("YES")
        
        