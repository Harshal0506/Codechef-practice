T=int(input())
for _ in range(T):
    B=int(input())
    Actual_Base=B-2 if (B>=2) else 0
    Base_Box=Actual_Base//2
    Total_Box=Base_Box*(Base_Box+1)//2
    print(Total_Box)