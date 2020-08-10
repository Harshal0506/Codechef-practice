T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    A=set(list(map(int,input().split())))
    B=set(list(map(int,input().split())))
    print(len(A.intersection(B)))