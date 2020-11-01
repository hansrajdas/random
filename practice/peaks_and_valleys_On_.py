def peaks_and_valleys(A):
    idx = 1
    while idx < len(A):
        if A[idx - 1] < A[idx]:
            A[idx - 1], A[idx] = A[idx], A[idx - 1]

        if idx < len(A) - 1 and A[idx] > A[idx + 1]:
            A[idx], A[idx + 1] = A[idx + 1], A[idx]
        idx += 2

A = [5, 3, 1, 2, 3] 
print(A)
peaks_and_valleys(A)
print(A)

A = list(range(9))
print(A)
peaks_and_valleys(A)
print(A)

A = list(range(10))
print(A)
peaks_and_valleys(A)
print(A)
