T=int(input())
for _ in range(T):
    input()
    V=list(map(int,input().split()))
    V.sort()
    min=V[-1]
    for i in range(1,len(V)):
        if V[i]-V[i-1]<min:
            min=V[i]-V[i-1]
        if min==0:
            break
    print(min)
