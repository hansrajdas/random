def search_min(A):
    if not A:
        raise ValueError('Empty list')
    left = 0
    right = len(A) - 1

    while True:
        mid = left + (right - left) // 2

        if left >= right:
            return A[mid]

        if mid < right and A[mid] > A[mid + 1]:
            return A[mid + 1]
        if mid > left and A[mid - 1] > A[mid]:
            return A[mid]
        if A[mid] < A[right]:
            right = mid - 1
        else:
            left = mid + 1

assert search_min([1, 2, 3, 4, 5, 6, 7, 8]) == 1
assert search_min([1]) == 1
assert search_min([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]) == 1
assert search_min([2, 2, 2, 3, 4, 2]) == 2
