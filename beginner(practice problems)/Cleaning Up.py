T=int(input())
for _ in range(T):
    n,m=list(map(int,input().split()))
    done=list(map(int,input().split()))
    Todo=[i for i in range(1,n+1)]
    final=set(Todo).difference(set(done))
    final=list(final)
    final.sort()
    for i in final[0:len(final):2]:
        print(i,end=" ")
    print('')
    for i in final[1:len(final):2]:
        print(i,end=" ")
    print('')