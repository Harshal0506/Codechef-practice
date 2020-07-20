# cook your dish here
years_with_31_days=[1,3,5,7,8,10,12]
def isLeap(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

T=int(input())
for _ in range(T):
    year,month,day=list(map(int,input().split(":")))
    if month in years_with_31_days:
        Total=(31-day)//2+1
    elif month==2:
        if isLeap(year):
            Total=(29-day)//2+1
        else:
            if day%2==0:
                Total=(28-day)//2+1+15
            else:
                Total=(28-day)//2+1+16
    else:
        if day%2==0:
            Total=(30-day)//2+1+15
        else:
            Total=(30-day)//2+1+16
    
    print(Total)
    
    