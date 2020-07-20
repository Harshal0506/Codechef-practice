#https://www.codechef.com/problems/ISITCAKE 
T=int(input())
for _ in range(T):
    count=0
    for _ in range(10):
        L=list(map(int,input().split()))
        for i in L:
            if i<=30:
                count+=1
    if count>=60:
        print("yes")
    else:
        print("no")
                
        
