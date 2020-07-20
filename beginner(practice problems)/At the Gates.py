# cook your dish here
T=int(input())
for _ in range(T):
    ruler='H'
    N,K=list(map(int,input().split()))
    coin=input().split()
    
    for i in range(K):
        if coin[-1]==ruler:
            if ruler=='H':
                ruler='T'
            else:
                ruler='H'
            coin.pop()
        else:
            coin.pop()
    
    print(coin.count(ruler))