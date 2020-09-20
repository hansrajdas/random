def logn(n, b):
    if n < b:
        return 0
    return 1 + logn(n // b, b)
