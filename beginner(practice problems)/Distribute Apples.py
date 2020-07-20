# cook your dish here
T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    if (N%(K*K)==0):
        print("NO")
    else:
        print("YES")
    