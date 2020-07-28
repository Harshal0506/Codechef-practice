T=int(input())
for _ in range(T):
    L=list(input())
    if L.count('1')==1 or L.count('0')==1:
        print("Yes")
    else:
        print("No")