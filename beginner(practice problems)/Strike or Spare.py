T=int(input())
for _ in range(T):
    N=int(input())
    if N%2==0:
        print(1,10**(N//2))
    else:
        print(1,10**((N+1)//2-1))