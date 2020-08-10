t=int(input())
for i in range(t):
    mx = 0
    t2=int(input())
    for k in range(t2):
        m,n,o=map(int,input().split())
        l=(n//(m+1))*o
        if(l>mx):
            mx=l
    print(mx)