T=int(input())
for _ in range(T):
    N,k=list(map(int,input().split()))
    A=list(map(int,input().split()))
    final=''
    for i in A:
        if k-i>=0:
            final+='1'
            k-=i
        else:
            final+='0'
    print(final)