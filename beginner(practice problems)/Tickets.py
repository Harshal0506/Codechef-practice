# cook your dish here
T=int(input())
for _ in range(T):
    flag=1
    s=list(input())
    if s[0]==s[1]:
        flag=0
    if flag==1:
        for i in range(2,len(s),2):
            if s[i]!=s[0]:
                flag=0
                break
    if flag==1:
        for i in range(3,len(s),2):
            if s[i]!=s[1]:
                flag=0
                break
    if flag==1:
        print("YES")
    else:
        print("NO")
            
        
    
    