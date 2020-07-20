a,b= map(int, input().split(' '))
c=0
for i in range(a):
    k=int(input())
    if(k%b==0):
        c=c+1
print(c)