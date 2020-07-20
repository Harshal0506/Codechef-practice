
T=int(input())
for _ in range(T):
    L=list(map(int,input().split()))
    P=L.pop()
    Totalhours= sum(L)*P
    if Totalhours>120:
        print("Yes")
    else:
        print("No")