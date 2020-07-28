T=int(input())
for _ in range(T):
    A=list(map(int,input().split()))
    A.remove(len(A)-1)

    print(max(A))