# cook your dish here
T=int(input())
for _ in range(T):
    quantity,price=list(map(int,input().split()))
    if quantity>1000:
        print("{:.6f}".format(0.9*quantity*price))
    else:
        print("{:.6f}".format(quantity*price))