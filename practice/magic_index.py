def get_magic_index(A, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if mid == A[mid]:
        return mid
    if mid > A[mid]:
        return get_magic_index(A, mid + 1, right)
    return get_magic_index(A, left, mid - 1)

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
