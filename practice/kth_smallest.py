def partition(A, low, high):
    i = low
    j = low
    pivot = A[high]
    while j < high:
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[i], A[high] = A[high], A[i]
    return i

def kthSmallest(A, low, high, k):
    if k > 0 and k <= high - low + 1:
        pi = partition(A, low, high)
        if pi - low == k - 1:
            return A[pi]
        if pi - low > k - 1:
            return kthSmallest(A, low, pi - 1, k)
        return kthSmallest(A, pi + 1, high, k - pi + low - 1)
    return None

A = [12, 3, 5, 7, 4, 19, 26]
assert kthSmallest(A, 0, len(A) - 1, 3) == 5
assert kthSmallest(A, 0, len(A) - 1, 4) == 7
assert kthSmallest(A, 0, len(A) - 1, 7) == 26
assert kthSmallest(A, 0, len(A) - 1, 8) == None
