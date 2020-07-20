T=int(input())
for _ in range(T):
    N=int(input())
    S=list(map(int,input().split()))
    C1=0
    for i in S:
        if i==1:
            C1+=1
        elif C1>0:
            C1-=1
        else:
            print("Invalid")
            break
    else:
        print("Valid")


