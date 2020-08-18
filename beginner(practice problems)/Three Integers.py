T=int(input())
for _ in range(T):
    A,B,C=list(map(int,input().split()))
    T=0
    if((A+C)%2==1 ):
        T+=1
        T+=min([abs((A+C)//2-B),abs((A+C+1)//2-B)])
        
        
    else:
        T+=abs((A+C)//2 - B)
    
    print(T)