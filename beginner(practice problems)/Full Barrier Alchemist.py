# cook your dish here
T=int(input())
for _ in range(T):
    N,H,Y1,Y2,L=list(map(int,input().split()))
    greater=Y2
    smaller=H-Y1
    count=0
    flag=1
    for i in range(N):
        t,x=list(map(int,input().split()))
        if flag==1:
            if t==1:
                if x<smaller:
                    L-=1
                    if (L!=0):
                        count+=1
                    else:
                        flag=0
                        continue
                else:
                    count+=1
            else:
                if x>greater:
                    L-=1
                    if L!=0:
                        count+=1
                    else:
                        flag=0
                        continue
                else:
                    count+=1
    print(count)    
        
        
        