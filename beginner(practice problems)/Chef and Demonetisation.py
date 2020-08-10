T=int(input())
for _ in range(T):
    S,N=list(map(int,input().split()))
    TotalNotes=0
    if S%2==1:
        TotalNotes+=1
        S-=1
    if S!=0:
        if N>=S:
            TotalNotes+=1
        else:
            TotalNotes+=S//N
            S%=N
            if S!=0:
                TotalNotes+=1
    print(TotalNotes)
    