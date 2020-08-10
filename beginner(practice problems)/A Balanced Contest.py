T=int(input())
for _ in range(T):
    N,P=list(map(int,input().split()))
    Solver=list(map(int,input().split()))
    CakeWalk=0
    Hard=0
    for i in Solver:
        if i>=P//2:
            CakeWalk+=1
            
        if i<=P//10:
            Hard+=1
        
        if CakeWalk==2 or Hard==3:
            break
    if CakeWalk==1 and Hard==2:
        print("yes")
    else:
        print("no")