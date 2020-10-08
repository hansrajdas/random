def max_profit(A, n, d):
    if not n:
        return 0
    if n in d:
        return d[n]
    mp = A[n - 1]
    for i in range(1, n):
        mp = max(mp, max_profit(A, i, d) + max_profit(A, n - i, d))
    d[n] = mp
    return mp

print(max_profit([1, 5, 8, 9, 10, 17, 17, 20], 8, {}))  # 22 -> 5*2 + 17*6
print(max_profit([3, 5, 8, 9, 10, 17, 17, 20], 8, {})) # 24 ->  3*8
print(max_profit(range(50), 50, {}))  # 49
