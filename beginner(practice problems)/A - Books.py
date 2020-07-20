T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    B=[]
    prev=-1

    while(prev<len(A)-1):
        curr=prev+1
        N-=1
        while(curr<len(A)-1 and (A[curr]==A[curr+1])):
            curr+=1
            N-=1
        count=curr-prev
        B.extend([N]*count)
        prev=curr
    for i in B:
        print(i,end=" ")
    print()

