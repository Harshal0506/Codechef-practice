T=int(input())
for _ in range(T):
    N=int(input())
    final={}
    for i in range(N):
        s,i=input().split()
        i=int(i)
        if i==0:
            final[s]=final.get(s,[0,0])
            final[s][0]+=1

        else:
            final[s]=final.get(s,[0, 0])
            final[s][1]+=1
    s=0
    for i in final:
        s+=max(final[i])
    print(s)