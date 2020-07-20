# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    remainder=N%8
    if remainder==7:
        partner=N+1
    elif remainder==0:
        partner=N-1
    elif remainder<=3:
        partner=N+3
    else:
        partner=N-3
    
    if remainder==1 or remainder==4:
        print("{}LB".format(partner))
    elif remainder==2 or remainder==5:
        print("{}MB".format(partner))
    elif remainder==3 or remainder==6:
        print("{}UB".format(partner))
    elif remainder==7:
        print("{}SU".format(partner))
    else:
         print("{}SL".format(partner))