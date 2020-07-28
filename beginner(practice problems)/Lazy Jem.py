for _ in range(int(input())):
    n, b, m = map(int, input().split())
    t = 0
    while n > 0:
        if n % 2 == 0:
            h = n // 2
        else:
            h = (n + 1) // 2

        t = t + m * h + b
        n = n - h
        m = m * 2

    # since one extra b added
    t = t - b
    print(t)