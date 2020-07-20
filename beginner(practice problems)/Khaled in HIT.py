T = int(input())
for _ in range(T):
    N = int(input())
    M = N // 4

    F = []
    A = list(map(int, input().split()))
    A.sort()
    if M > 1:

        for i in range(M, len(A), M):

            if A[i + 1] == A[i]:
                F = [-1]
                break
            else:
                F.append(A[i])
    else:
        if len(set(A)) == len(A):
            F = A[1:]
        else:
            F = [-1]
    if len(F) == 1:
        print("-1")
    else:
        print("{} {} {}".format(F[0], F[1], F[2]))

