T=int(input())
for _ in range(T):
    s=input()
    if len(s)%2!=0:
        print('no')
    else:
        for i in range(0,len(s),2):
            if s[i]==s[i+1]:
                print('no')
                break
        else:
            print('yes')