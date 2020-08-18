T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    old=input().split()
    Letters=[]
    for i in range(K):
        Letters.extend(input().split()[1:])
    for i in old:
        if i in Letters:
            print("YES" ,end=" ")
        else:
            print("NO",end=" ")
    print('')
            
        