T=int(input())
for _ in range(T):
    N,R=list(map(int,input().split()))
    A=list(map(int,input().split()))
    mini=0
    maxi=1000000001
    for i in A:
        if i == R:
            print("YES")
        else:
            if i>mini and i<maxi:
                if i<R:
                    mini=i
                else:
                    maxi=i
            else:
                print("NO")
                break
