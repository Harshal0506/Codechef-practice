
T=int(input())
for _ in range(T):
    L=list(map(int,input().split()))
    if ((L[0]+L[1])//L[2])%2:
        print("COOK")
        
    else:
        
        print("CHEF")
    
