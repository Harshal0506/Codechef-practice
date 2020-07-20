T=int(input())
for _ in range(T):
    L=list(map(int,input().split()))
    for i in range(2):
        if (L[i]>L[i+1] and L[3+i]>L[4+i]) or (L[i]<L[i+1] and L[3+i]<L[4+i]) or (L[i]==L[i+1] and L[3+i]==L[4+i]):
            pass
        else:
            print("NOT FAIR")
            break
    else:
        if (L[0]>L[2] and L[3]>L[5]) or (L[0]<L[2] and L[3]<L[5]) or (L[0]==L[2] and L[3]==L[5]):
            print("FAIR")
        else:
            print("NOT FAIR")



