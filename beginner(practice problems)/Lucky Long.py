t=int(input())
while(t):
    n=input().strip()
    c=0
    for i in n:
        if i is not "7" and i is not "4":
            c=c+1
    print(c)
    t=t-1