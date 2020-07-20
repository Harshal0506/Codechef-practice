# cook your dish here
T=int(input())
for _ in range(T):
    l,r,k=list(map(int,input().split()))
    if l==r:
        print(1)
    else:
        print(k)