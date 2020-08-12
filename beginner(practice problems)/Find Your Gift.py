T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    x=0
    y=0
    prev=' '
    for i in S:
        if prev in [' ','L','R'] and i in ['U','D']:
            if i=='U':
                y+=1
            else:
                y-=1
            prev=i
        if prev in [' ','U','D'] and i in ['L','R']:
            if i=='L':
                x-=1
            else:
                x+=1
            prev=i
    print(x,y)