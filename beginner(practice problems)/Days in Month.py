week_dictonaty=["mon","tues","wed","thurs","fri","sat","sun"]
T=int(input())
for _ in range(T):
    w,s=input().split()
    w=int(w)

    A=[w//7]*7
    i=week_dictonaty.index(s)
    for a in range(w%7):
        A[i%7]+=1
        i+=1
    for i in A:
        print(i,end=" ")
    print()