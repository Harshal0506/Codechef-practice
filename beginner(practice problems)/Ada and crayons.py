# cook your dish here
T=int(input())
for _ in range(T):
    c=list(input())
    U=0
    D=0
    if c[0]=='U':
        U+=1
    else:
        D+=1
    for i in range(1,len(c)):
        if c[i-1]!=c[i]:
            if c[i]=="U":
                U+=1
            else:
                D+=1
    print(min([U,D]))
        