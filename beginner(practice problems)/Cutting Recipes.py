# cook your dish here
from math import gcd
T=int(input())
for _ in range(T):
    L=list(map(int,input().split()))
    if len(L)==2:
        G=L[1]
    else:
        G=gcd(L[1],L[2])
        for i in range(3,len(L)):
            G=gcd(L[i],G)
    for i in L[1:]:
        print(i//G,end=" ")
    print()
        
        