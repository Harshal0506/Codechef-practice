for _ in range(int(input())):
    [n, m] = list(map(int, input().split(" ")))
    [h, v, s] = list(map(int, input().split(" ")))
    h_rivers = v_rivers = []
    if h: h_rivers = list(map(int, input().split(" ")))
    if v: v_rivers = list(map(int, input().split(" ")))
    v_count = h_count = 0
    prev = 0
    for i in h_rivers:
        h_count += (i - prev - 1) // s
        prev = i
    h_count += (n - prev) // s
    prev = 0
    for i in v_rivers:
        v_count += (i - prev - 1) // s
        prev = i
    v_count += (m - prev) // s
    print(h_count * v_count)
