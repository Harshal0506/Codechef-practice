T=int(input())
for _ in range(T):
    n=int(input())
    d=list(map(int,input().split()))
    print(len(set(d)))