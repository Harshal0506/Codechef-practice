T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    upper=0
    lower=0
    Message=input()
    for i in Message:
        if i.isupper():
            upper+=1
    lower=len(Message)-upper
    if upper<=K and lower<=K:
        print("both")
    elif upper>K and lower<=K:
        print("brother")
    elif lower>K and upper<=K:
        print("chef")
    else:
        print("none")