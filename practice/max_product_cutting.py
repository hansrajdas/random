def getMaxProduct(n, d):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    if n in d:
        return d[n]
    _max = 1
    for i in range(2, n):
        _max = max(_max, i * (n - i), i * getMaxProduct(n - i, d))
        d[n] = _max
    return _max

# Main
print(getMaxProduct(2, {'k': 1}))  # 1 -> 1*1
print(getMaxProduct(3, {'k': 1}))  # 2 -> 1*2
print(getMaxProduct(4, {'k': 1}))  # 4 -> 2*2
print(getMaxProduct(5, {'k': 1}))  # 6 -> 2*3
print(getMaxProduct(9, {'k': 1}))  # 9 -> 3*3*3
print(getMaxProduct(10, {'k': 1}))  # 36 -> 3*3*4
print(getMaxProduct(50, {'k': 1}))  # 86093442
