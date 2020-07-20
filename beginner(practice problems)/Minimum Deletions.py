# cook your dish here
import math
T=int(input())
for _ in range(T):
    input()
    a=list(map(int,input().split()))
    result=a[0]
    for i in a[1:]:
        result=math.gcd(i,result)
        if result==1:
            print(0)
            break
    else:
        print(-1)