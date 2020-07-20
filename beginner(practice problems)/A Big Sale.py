# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    TotalLoss=0
    for i in range(N):
        price,quantity,discount=list(map(int,input().split()))
        new_price=((100-discount)*(100+discount)*price)/10000
        Loss=price-new_price
        Loss=Loss*quantity
        TotalLoss+=Loss
    print("{:.2f}".format(TotalLoss))