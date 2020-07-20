# cook your dish here
T=int(input())
for _ in range(T):
    N,U,D=list(map(int,input().split()))
    H=list(map(int,input().split()))
    Hill=1
    para=1
    for i in range(N-1):
        if H[i+1]==H[i]:
            Hill+=1
        elif H[i+1]>H[i] and H[i+1]-H[i]<=U:
            Hill+=1
        elif H[i+1]<H[i] and H[i]-H[i+1]<=D:
            Hill+=1
        elif H[i+1]<H[i] and para==1:
            Hill+=1
            para=0
        else:
            break
    print(Hill)
        