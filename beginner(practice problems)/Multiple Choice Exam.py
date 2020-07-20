T=int(input())
for _ in range(T):
    N=int(input())
    C=input()
    U=input()
    i=0
    points=0
    while i<N:
        if U[i]=="N":
            i+=1
        elif U[i]==C[i]:
            points+=1
            i+=1
        else:
            i+=2
    print(points)


