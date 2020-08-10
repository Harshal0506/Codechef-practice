N=int(input())
A=list(map(int,input().split()))
E=0
for i in A:
    if i%2==0:
        E+=1
O=N-E
if E>O:
    print("READY FOR BATTLE")
else:
    print("NOT READY")