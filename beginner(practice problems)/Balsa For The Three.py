T=int(input())
for _ in range(T):
    N=int(input())
    for i in range(N+1,N+1001):
        if str(i).count('3')>=3:
            print(i)
            break
            