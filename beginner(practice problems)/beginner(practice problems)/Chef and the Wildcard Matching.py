T=int(input())
for _ in range(T):
    X=input()
    Y=input()
    for i in range(len(X)):
        if X[i]=='?' or Y[i]=='?':
            continue
        if X[i]!=Y[i]:
            print('No')
            break
    else:
        print('Yes')