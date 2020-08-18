T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.remove(max(A))
    B.remove(max(B))
    if sum(A)<sum(B):
        print('Alice')
    elif sum(A)>sum(B):
        print('Bob')
    else:
        print('Draw')