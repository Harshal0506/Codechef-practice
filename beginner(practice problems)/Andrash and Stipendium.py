T=int(input())
for _ in range(T):
    flag=0
    N=int(input())
    R=list(map(int,input().split()))
    if 2 not in R:
        if 5 in R:
            if sum(R)/N>=4:
                print("Yes")
                flag=1
    if flag==0:
        print("No")