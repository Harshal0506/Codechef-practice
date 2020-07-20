Jeff=input()
N=int(input())
for _ in range(N):
    word=input()
    for letter in word:
        if letter not in Jeff:
            print("No")
            break
    else:
        print("Yes")


