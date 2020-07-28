T=int(input())
for _ in range(T):
    finish,distancetoBolt,tigerAccelaration,boltSpeed=list(map(int,input().split()))
    Tb=finish/boltSpeed
    Tt=(2*(finish+distancetoBolt)/tigerAccelaration)**0.5
    if Tb<Tt:
        print("Bolt")
    else:
        print("Tiger")