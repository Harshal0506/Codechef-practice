T=int(input())
for _ in range(T):
    ans=''
    a,b=list(input().split())
    La=len(a)
    Lb=len(b)
    if La>Lb:
        b='0'*(La-Lb)+b
    else:
        a='0'*(Lb-La)+a
    for i in range(len(a)):
        ans+=str((int(a[i])+int(b[i]))%10)
    
    print(int(ans))
   