def sort_0_1_and_2(A):
    low = 0
    mid = 0
    high = len(A) - 1
    while mid <= high:
        if A[mid] == 0:
            A[mid], A[low] = A[low], A[mid]
            low += 1
            mid += 1
        elif A[mid] == 2:
            A[mid], A[high] = A[high], A[mid]
            high -= 1
        else:
            mid += 1
    return A

assert sort_0_1_and_2([0, 1, 2]) == [0, 1, 2]
assert sort_0_1_and_2([0, 0, 1, 1, 2, 2]) == [0, 0, 1, 1, 2, 2]
assert sort_0_1_and_2([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
assert sort_0_1_and_2([2, 1, 2, 0, 0, 1, 0, 1]) == [0, 0, 0, 1, 1, 1, 2, 2]
