# cook your dish here
T=int(input())
for _ in range(T):
    N=int(input())
    S=input().split()
    for i in range(N):
        if S[i] == "cookie":
            if  i<N-1 and S[i+1]=="milk":
                continue
            else:
                print("NO")
                break
    else:
        print("YES")
            