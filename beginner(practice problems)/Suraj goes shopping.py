T=int(input())
for _ in range(T):
    N=int(input())
    Cost=list(map(int,input().split()))
    Cost.sort(reverse=True)
    i=0
    Total=0
    while(i<len(Cost)):
        Total+=Cost[i]
        if i+1<len(Cost):
            Total+=Cost[i+1]
        i+=4
    print(Total)
        