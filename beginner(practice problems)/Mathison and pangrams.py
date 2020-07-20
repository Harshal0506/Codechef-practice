T=int(input())
for _ in range(T):
    L=[0]*26
    Total=0
    M=list(map(int,input().split()))
    for i in input():
        if L[ord(i)-97]==0:
            L[ord(i)-97]+=1
    for i in range(26):
        if L[i]==0:
            Total+=M[i]
    print(Total)


