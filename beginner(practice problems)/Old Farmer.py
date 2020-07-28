T=int(input())
for _ in range(T):
    N,M=list(map(int,input().split()))
    F=[]
    for k in range(N):
        F.append(list(map(int,input().split())))
    max=0
    for i in range(N-1):

        for j in range(i+1,N):
            for a in range(M):
                sum=0
                x=M-1
                while(x>a):
                    sum+=(F[i][x]+F[j][x])
                    x-=1
                y=i
                while(y<=j):
                    sum+=(F[y][a])
                    y+=1
                if sum>max:
                    max=sum
    print(max)





