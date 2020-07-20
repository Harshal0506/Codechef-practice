T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    i=0
    
    while i<N:
        count=1
        
        while(i<N-1 and A[i+1]*A[i]<0):
            count+=1
            i+=1
        
        
        while(count>0):
            print(count,end=" ")
            count-=1
        
        i+=1
    print("")
        