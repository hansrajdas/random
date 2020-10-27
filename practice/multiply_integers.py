def multiply(bigger, smaller):
    if bigger < smaller:
        return multiply(smaller, bigger)
    if not smaller:
        return 0
    if smaller == 1:
        return bigger
    half_product = multiply(bigger, smaller // 2)
    if smaller % 2:
        return bigger + (half_product << 1)
    return half_product << 1

assert multiply(5, 0) == 0
assert multiply(5, 1) == 5
assert multiply(5, 2) == 10
assert multiply(5, 3) == 15
assert multiply(5, 4) == 20
assert multiply(5, 5) == 25
