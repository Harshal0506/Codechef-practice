# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    zero=0
    two=0
    for i in A:
        if i==0:
            zero+=1
        elif i==2:
            two+=1
    
    Total=(zero*(zero-1))//2+(two*(two-1))//2
    print(Total)