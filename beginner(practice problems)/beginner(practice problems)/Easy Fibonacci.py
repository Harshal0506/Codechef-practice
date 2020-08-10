import math
T=int(input())
fib=[0,1]
for i in range(2,60):
    fib.append((fib[i-1]+fib[i-2])%10)
for _ in range(T):
    N=int(input())
    P=math.floor(math.log(N,2))
    Position=(2**P-1)%60
    print(fib[Position])
    