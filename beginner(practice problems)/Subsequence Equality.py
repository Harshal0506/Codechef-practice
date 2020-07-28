T=int(input())
for _ in range(T):
    S=list(input())
    if len(S)==len(set(S)):
        print("no")
    else:
        print("yes")