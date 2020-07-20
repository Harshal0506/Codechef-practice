# cook your dish here
T=int(input())
for _ in range(T):
    S,w1,w2,w3=list(map(int,input().split()))
    if sum([w1,w2,w3])<=S:
        print(1)
    elif w1+w2<=S or w2+w3<=S:
        print(2)
    else:
        print(3)