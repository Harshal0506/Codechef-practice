

T=int(input())

for _ in range(T):
    i=int(input())
    L=[]
    for _ in range(i):
        L.append([0]*i)
    num=1
    for a in range(i):
        for b in range(a,-1,-1):
            L[a-b][b]=num;
            num+=1
    for a in range(1,i,1):
        c=0
        for b in range(a,i,1):
            
            L[b][i-c-1]=num
            num+=1
            c+=1
    
    for i in range(i):
        L[i]=" ".join(list(map(str,L[i])))
        print(L[i])
