T=int(input())
for _ in range(T):
    a,b,c,d=list(map(int,input().split()))
    final=[]
    for i in [a,b,c,d]:
        if i not in final:
           final.append(i)
        else:
            final.remove(i)
    if len(final)==0:
        print("YES")
    else:
        print("NO")
            
           