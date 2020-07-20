T=int(input())
for _ in range(T):
    s=list(input())
    flag=0
    i=0
    while i<len(s):
        if s[i]=="1" and flag==1:
            flag=0
            break
        if s[i]=="1":
            flag=1
            while(i<len(s)-1 and  s[i+1]=="1"):
                i+=1
        i+=1
    if flag==0:
        print("NO")
    else:
        print("YES")


