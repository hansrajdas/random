def get_magic_index(A, left, right):
    if left > right:
        return -1
    m = left + (right - left) // 2
    if A[m] == m:
        return m
    right_idx = get_magic_index(A, max(m + 1, A[m]), right)
    if right_idx != -1:
        return right_idx
    return get_magic_index(A, left, min(A[m], m - 1))


def solve(A):
    return get_magic_index(A, 0, len(A) - 1)

assert solve([]) == -1
assert solve([1]) == -1
assert solve([0]) == 0
assert solve([-1, 1, 3]) == 1
assert solve([-4, 1, 2, 3]) == 1
assert solve([-4, -2, 1, 3]) == 3
assert solve([0, 2, 3, 5]) == 0
assert solve([2, 3]) == -1
assert solve([-1, 1]) == 1

# Dups
assert solve([10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]) == 2
