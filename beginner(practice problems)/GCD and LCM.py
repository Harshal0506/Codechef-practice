# cook your dish here
import math
T=int(input())
for _ in range(T):
    A,B=list(map(int,input().split()))
    G=math.gcd(A,B)
    L=(A*B)//G
    print(G,L)