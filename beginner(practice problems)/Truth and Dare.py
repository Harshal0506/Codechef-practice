# cook your dish here
T=int(input())
for _ in range(T):
    input()
    ramTruth=set(list(map(int,input().split())))
    input()
    ramDare=set(list(map(int,input().split())))
    input()
    shyamT=set(list(map(int,input().split())))
    input()
    shyamD=set(list(map(int,input().split())))
    if len(shyamT.difference(ramTruth))==0 and len(shyamD.difference(ramDare))==0:
        print("yes")
    else:
        print("no")