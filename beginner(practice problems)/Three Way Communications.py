import math


def distance(x1, y1, x2, y2):
    # Calculating distance
    return  math.sqrt(math.pow(x2 - x1, 2) +
                     math.pow(y2 - y1, 2) * 1.0)



T=int(input())
for _ in range(T):
    R=int(input())
    P1=list(map(int,input().split()))
    P2 =list(map(int, input().split()))
    P3 =list(map(int, input().split()))
    Count=0
    if Count<2 and distance(P1[0],P1[1],P2[0],P2[1])<=R:
        Count+=1
    if Count<2 and distance(P3[0],P3[1],P2[0],P2[1])<=R:
        Count+=1
    if Count<2 and distance(P3[0],P3[1],P1[0],P1[1])<=R:
        Count+=1
    if Count<2:
        print("no")
    else:
        print("yes")