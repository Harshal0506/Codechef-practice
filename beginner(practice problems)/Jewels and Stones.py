T=int(input())
for _ in range(T):
    J=input()
    S=input()
    Total=0
    for i in set(J):
        Total+=S.count(i)
    print(Total)
    