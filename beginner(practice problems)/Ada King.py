T=int(input())
for _ in range(T):
    K=int(input())-1
    for i in range(8):
        for j in range(8):
            if i==0 and j==0:
                print('O',end="")
            elif K>0:
                print('.',end="")
                K-=1
            else:
                print('X',end="")
        print()

