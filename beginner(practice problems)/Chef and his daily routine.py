T=int(input())
for _ in range(T):
    Observation=list(input())
    for i in range(1,len(Observation)):
        if Observation[i]<Observation[i-1]:
            print("no")
            break
    else:
        print("yes")
