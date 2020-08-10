N=int(input())
Maxi=0
W=None
S,T=0,0
for _ in range(N):
    SH,TH=list(map(int,input().split()))
    S+=SH
    T+=TH
    L=abs(S-T)
    if L>Maxi:
        Maxi=L
        W =1 if (S>T)else 2
print(W,Maxi)
        