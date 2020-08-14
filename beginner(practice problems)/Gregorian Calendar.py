import calendar
WeekDay=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

T=int(input())
for _ in range(T):
    year=int(input())
    Count=0
    if year >=2001:
        for i in range(2001,year):
            if calendar.isleap(i):
                Count+=2
            else:
                Count+=1
                
        print(WeekDay[Count%7])
    else:
        for i in range(2000,year-1,-1):
            if calendar.isleap(i):
                Count-=2
            else:
                Count-=1
        print(WeekDay[Count%7])