def F(A):
    balance = 0
    maxbalance = 0
    for i in A:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        maxbalance = max([maxbalance, balance])

    return maxbalance


T = int(input())
for _ in range(T):
    A = input()
    N = F(A)
    B = "(" * N
    B += ')' * N
    print(B)