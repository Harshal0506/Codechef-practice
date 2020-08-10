T=int(input())
for _ in range(T):
    A=[]
    N=int(input())
    for i in range(N):
        A.append(list(map(int,input().split())))
    maximum=sum([A[n][n]  for n in range(N)])
    for j in range(1,N):
        sumy=0
        for x in range(N-j):
            sumy+=A[x][x+j]
        if sumy>maximum:
            maximum=sumy
        sumy=0
        for y in range(N-j):
            sumy+=A[y+j][y]
        if sumy>maximum:
            maximum=sumy
            
    print(maximum)
            
    
    
        