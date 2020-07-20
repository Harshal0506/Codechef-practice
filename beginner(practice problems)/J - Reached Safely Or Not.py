# cook your dish here
T=int(input())
for j in range(1,T+1):
    m,n=list(map(int,input().split()))
    rx,ry=list(map(int,input().split()))
    N=int(input())
    D=list(input())
    x=0
    y=0
    for i in D:
        if i=="U":
            y+=1
        elif i=="D":
            y-=1
        elif i=="R":
            x+=1
        else:
            x-=1
    if [x,y]==[rx,ry]:
        data="REACHED"
    elif x<0 or x>m or y<0 or y>n:
        data="DANGER"
    else:
        data="SOMEWHERE"
    print("Case {}: {}".format(j,data))