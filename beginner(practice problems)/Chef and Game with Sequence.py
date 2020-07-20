# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    even=0

    for i in list(map(int,input().split())):
        if i%2==0:
            even+=1
    odd=N-even
    count=0
    if odd%2==1:
        count+=1
    if even>0 or odd>1:
        count+=1
    print(count)