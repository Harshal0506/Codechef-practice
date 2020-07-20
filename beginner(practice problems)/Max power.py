# cook your dish here
N=int(input())
X=list(map(int,list(input())))
Count=0
for i in range(N-1,-1,-1):
    if X[i]==1:
        Count=N-1-i
        break
print(Count)