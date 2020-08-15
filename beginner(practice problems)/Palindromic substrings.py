# cook your dish here
T=int(input())
for _ in range(T):
    A=input()
    B=input()
    if len(set(A).intersection(set(B)))==0:
        print('No')
    else:
        print('Yes')