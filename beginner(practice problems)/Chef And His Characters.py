T=int(input())
req=list('chef')
req.sort()
for _ in range(T):
    s=list(input())
    found=0
    
    
    for i in range(len(s)-3):
        A=s[i:i+4]
        A.sort()
        if A==req:
            found+=1
    if found==0:
        print('normal')
    else:
        print("lovely",found)
        
        