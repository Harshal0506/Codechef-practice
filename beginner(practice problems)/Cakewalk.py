T=int(input())
for _ in range(T):
    N=int(input())
    Count10=0
    Count2=0
    while(N%10==0):
        Count10+=1
        N=N//10
    while(N%2==0):
        Count2+=1
        N=N//2
    if N==1 and Count2<=Count10:
        print("Yes")
    else:
        print("No")