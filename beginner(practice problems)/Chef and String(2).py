T=int(input())
for _ in range(T):
    s=input()
    if s[1:]+s[0]== s[-1]+s[0:-1]:
        print("YES")
    else:
        print("NO")