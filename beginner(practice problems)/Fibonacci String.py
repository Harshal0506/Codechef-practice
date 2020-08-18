T=int(input())
for _ in range(T):
    S=input()
    C=set(S)
    if len(C)<3:
        print("Dynamic")
    else:
        final=[S.count(i) for i in C]
        final.sort()
        t0=final[0]
        t1=final[1]
        for i in range(2,len(final)):
            assumed=t0+t1
            if assumed!=final[i]:
                print("Not")
                break
            t0=t1
            t1=assumed
        else:
            print("Dynamic")