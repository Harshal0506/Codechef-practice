T=int(input())
for _ in range(T):
    S1=input()
    S2=input()
    Count=0
    NotKnow=0
    for i in range(len(S1)):
        if S1[i]=='?' or S2[i]=='?':
            NotKnow+=1
        else:
            if S1[i]!=S2[i]:
                Count+=1
    print(Count,Count+NotKnow)
    