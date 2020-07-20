# cook your dish here
number=[]
N=int(input())
for _ in range(N):
    number.append(int(input()))
number.sort()
for i in number:
    print(i,end="\n")