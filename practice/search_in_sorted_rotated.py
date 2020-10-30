def search(A, k):
    if not A:
        return -1
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == k:
            return mid
        if A[left] <= A[mid]:  # Lower half is sorted
            if A[left] <= k and k < A[mid]:  # k is in lower half, search in lower half
                right = mid - 1
            else:
                left = mid + 1  # Search in higher half
        else:
            if A[mid] < k and k <= A[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

assert search([1, 2, 3, 4, 5, 6, 7, 8], 2) == 1
assert search([1, 2, 3, 4, 5, 6, 7, 8], 9) == -1
assert search([1, 2, 3, 4, 5, 6, 7, 8], 0) == -1
assert search([1], 0) == -1
assert search([1], 1) == 0
assert search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5) == 8
assert search([2, 2, 2, 3, 4, 2], 2) == 2
assert search([2, 2, 2, 3, 4, 2], 3) == 3
assert search([2, 2, 2, 3, 4, 2], 4) == 4
