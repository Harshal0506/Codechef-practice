# cook your dish here
from collections import Counter
T=int(input())
for _ in range(T):
    int(input())
    ingredent_used=[]
    flag=0
    recepie=list(map(int,input().split()))
    i=0
    while i<len(recepie):
        if recepie[i] not in ingredent_used:
            ingredent_used.append(recepie[i])
            while True:
                if i+1 != len(recepie) and recepie[i+1]==recepie[i]:
                    i+=1
                else:
                    i+=1
                    break
        else:
            
            flag=1
            break
            
    
    if flag==0:
        if len(Counter(recepie).values())==len(set(Counter(recepie).values())):
            print("YES")
        else:
            flag=1
            print("NO")
    else:
        print("NO")