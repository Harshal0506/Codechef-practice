
T=int(input())
for _ in range(T):
    GivenCake=[]
    price_red = 0
    price_green = 0
    N,M=list(map(int,input().split()))
    for i in range(N):
        GivenCake.append(list(input()))
    #redcake
    for i in range(0,N,2):
        for j in range(0,M,2):
            if GivenCake[i][j]!='R':
                price_red+=3
        for j in range(1,M,2):
            if GivenCake[i][j]!='G':
                price_red+=5
    for i in range(1,N,2):
        for j in range(0,M,2):
            if GivenCake[i][j]!='G':
                price_red+=5
        for j in range(1,M,2):
            if GivenCake[i][j]!='R':
                price_red+=3
    #greencake
    for i in range(0,N,2):
        for j in range(0,M,2):
            if GivenCake[i][j]!='G':
                price_green+=5
        for j in range(1,M,2):
            if GivenCake[i][j]!='R':
                price_green+=3
    for i in range(1,N,2):
        for j in range(0,M,2):
            if GivenCake[i][j]!='R':
                price_green+=3
        for j in range(1,M,2):
            if GivenCake[i][j]!='G':
                price_green+=5
    print(min([price_green,price_red]))






