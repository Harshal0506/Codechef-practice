# cook your dish here
N=int(input())
A=set(range(N+1))
B=set(list(map(int,input().split())))
A.difference_update(B)
for i in A:
    print(i,end=" ")