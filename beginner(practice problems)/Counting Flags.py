T=int(input())
for _ in range(T):
    N=int(input())
    Total=0
    if N-1>0:
        Total+=2*(N*(N-1)*(N-1))
    if N-2>0:
        Total+=(N*(N-1)*(N-2))+2*(N*(N-1)*(N-2)*(N-2))
    print(Total)