T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    M=int(input())
    B=list(map(int,input().split()))
    if M>N:
        print("No")
    else:
        for i in A:
            if len(B)!=0 and i==B[0]:
                B.pop(0)
        if len(B)==0:
            print("Yes")
        else:
            print("No")
                