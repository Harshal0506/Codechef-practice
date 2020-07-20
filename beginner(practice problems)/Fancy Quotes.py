# cook your dish here
T=int(input())
for _ in range(T):
    S=input().split()
    for i in S:
        if i=="not":
            print("Real Fancy")
            break
    else:
        print("regularly fancy")