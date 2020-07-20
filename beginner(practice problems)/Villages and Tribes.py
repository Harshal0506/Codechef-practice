# cook your dish here
T=int(input())
for _ in range(T):
    A=0
    B=0
    L=input()
    prev=None
    for i in range(len(L)):
        if L[i]==".":
            continue
        else:
            if L[i]=="A":
                if prev!=None and L[prev]==L[i]:
                
                    A+=(i-prev-1)
                A+=1
                prev=i
            else:
                if prev!=None and L[prev]==L[i]:
                
                    B+=(i-prev-1)
                B+=1
                prev=i
    print(A,B)
                
                