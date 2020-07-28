T=int(input())
for _ in range(T):
    flag=1
    L=int(input())
    S=input().strip('.')
    if S.startswith('H') and S.endswith('T'):
        prev='T'
        for i in S:
            if i == '.':
                continue
            else:
               if prev!=i:
                   prev=i
               else:
                   flag=0
                   break
    else:
        flag=0

    if flag==0:
        print("Invalid")
    else:
        print("Valid")
