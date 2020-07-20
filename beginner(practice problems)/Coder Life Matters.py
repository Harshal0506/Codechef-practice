T=int(input())
for _ in range(T):
    L=list(map(int,input().split()))
    Dayssteak=0
    for i in L:
        if i==1:
            if Dayssteak<5:
                Dayssteak+=1
            else:
                print("#coderlifematters")
                break
        else:
            Dayssteak=0
    else:
        print("#allcodersarefun")
            
                
            
        
