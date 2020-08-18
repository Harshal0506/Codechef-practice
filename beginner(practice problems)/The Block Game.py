t=int(input())
for _ in range(t):
    n=int(input())
    s=str(n)
    x=s
    if x==s[::-1]:
        print("wins")
    else:
        print("loses")