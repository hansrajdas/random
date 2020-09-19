# Find floor and ceil from unsorted array

def get_floor_ceil(A, x):
    floor = float('Inf')
    ceil = float('-Inf')
    for n in A:
        if n == x:
            return (x, x)
        elif n - x > 0:
            floor = min(floor, n)
        else:
            ceil = max(ceil, n)
    return (floor, ceil)

assert get_floor_ceil([1, 2, 3, 4, 5], 4) == (4, 4)
assert get_floor_ceil([1, 5, 3, 4, 10], 6) == (10, 5)
