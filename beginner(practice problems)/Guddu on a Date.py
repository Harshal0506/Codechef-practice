T=int(input())
for _  in range(T):
    N=int(input())
    N=str(N)
    Digit_sum=sum(list(map(int,list(N))))
    if Digit_sum%10==0:
        print(N+str(0))
    else:
        print(N+str(10-(Digit_sum%10)))
        
