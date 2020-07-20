# cook your dish here
T=int(input())
p1=0
p2=0
m,c=list(map(int,input().split()))
for _ in range(T):
    L=list(map(int,input().split()))
    if L[1]-m*L[0]-c>0:
        p1+=L[2]
    else:
        p2+=L[2]
print(max([p1,p2]))