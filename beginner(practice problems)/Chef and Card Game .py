T=int(input())
for _ in range(T):
    N=int(input())
    AT=0
    BT=0
    for i in range(N):
        A,B=list(map(str,input().split()))
        A=list(map(int,list(A)))
        A=sum(A)
        B= list(map(int, list(B)))
        B = sum(B)


        if A>B:
            AT+=1
        elif B>A:
            BT+=1
        else:
            AT+=1
            BT+=1
    if AT>BT:
        print(0,AT)
    elif BT>AT:
        print(1,BT)
    else:
        print(2,BT)
