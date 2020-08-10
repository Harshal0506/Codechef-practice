import math 
T=int(input())
for _ in range(T):
    N,A,B,K=list(map(int,input().split()))
    Lcm= (A*B)/math.gcd(A,B)
    
    Total=N//A +N//B - 2*(N//Lcm)
    if Total<K:
        print("Lose")
    else:
        print("Win")