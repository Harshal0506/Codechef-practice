T=int(input())
for _ in range(T):
    useful=0
    n,m=list(map(int,input().split()))
    A=list(map(int,input().split()))
    for i in A:
        if i%m==0:
            useful+=1
    print(2**useful-1)
