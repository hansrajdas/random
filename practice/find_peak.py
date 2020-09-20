def solve(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid == 0 and A[0] >= A[1]:
            return A[0]
        if mid == len(A) - 1 and A[len(A) - 1] >= A[len(A) - 2]:
            return A[mid]
        if A[mid - 1] <= A[mid] and A[mid] >= A[mid + 1]:
            return A[mid]
        if A[mid] > A[mid + 1]:
            high = mid - 1
        else:
            low = mid + 1

print(solve([1, 2, 3, 4]))
print(solve([5, 4, 3, 2, 1]))
print(solve([1, 2, 3, 4, 5]))
print(solve([1, 2, 3, 4, 5, 6]))
print(solve([4, 6, 2, 1]))
