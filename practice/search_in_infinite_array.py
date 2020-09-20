def binary_search(A, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search_in_infinite_array(A, x):
    low = 0
    high = 1
    while True:
        if A[low] <= x and A[high] >= x:
            return binary_search(A, low, high, x)
        elif A[low] < x and A[high] < x:
            low = high
            high <<= 1
        else:
            high = low
            low >>= 1
    return -1


assert search_in_infinite_array([1, 2, 3, 4, 5, 6, 7], 5) == 4
