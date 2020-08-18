# cook your dish here
def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True

T=int(input())
for _ in range(T):
    x,y=list(map(int,input().split()))
    i=x+y+1
    while True:
        if isPrime2(i):
            print(i-x-y)
            break
        i+=1
    