from collections import Counter
T=int(input())
for _ in range(T):
    Result=[]
    n=int(input())
    for i in range(n):
        Result.append(input())

    Result=Counter(Result)
    if n==0:
        print("Draw")
    elif len(set(Result.values()))==1 and len(Result.keys())==2:
        print("Draw")

    else:
        print(Result.most_common(1)[0][0])
