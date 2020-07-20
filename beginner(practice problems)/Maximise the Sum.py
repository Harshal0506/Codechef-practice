# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    sum_max=0
    for i in range(int(N/2)):
        sum_max+=(A[N-1-i]-A[i])
    print(sum_max)