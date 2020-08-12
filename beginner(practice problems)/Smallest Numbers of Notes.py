T=int(input())
for _ in range(T):
    N=int(input())
    Notes=0
    for i in [100,50,10,5,2,1]:
        Notes+=N//i
        N=N%i
    print(Notes)