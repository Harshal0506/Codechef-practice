T=int(input())
for _ in range(T):
    first=[]
    last=[]
    N=int(input())
    for i in range(N):
        F,L=input().split()
        first.append(F)
        last.append(L)
    
    for i in range(N):
        if first.count(first[i])==1:
            print(first[i])
        else:
            print(first[i],last[i])