S=int(input())
for _ in range(S):
    N=int(input())
    H=list(map(int,input().split()))
    if (N)%2==0:
        print("no")
    else:
        I=N-1
        rev=H[I//2+1:]
        rev.reverse()
        if H[:I//2 +1 ]==list(range(1,I//2 + 2)) and rev==list(range(1,I//2+1)):

            print("yes")
        else:

            print("no")

