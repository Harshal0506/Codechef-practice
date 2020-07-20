
T=int(input())
for _ in range(T):
    i=0
    product=0
    rating=0
    n=int(input())
    L=list(map(int,input().split()))
    R=list(map(int,input().split()))
    for j in range(n):

        if L[j]*R[j] > product:
            i=j
            product=L[j]*R[j]
            rating=R[j]
        elif L[j]*R[j]==product and R[j]>rating:
            i=j
            rating=R[j]
    print(i+1)