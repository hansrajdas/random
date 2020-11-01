def peaks_and_valleys(A):
    A.sort()

    idx = 0
    while idx < len(A) - 1:
        A[idx], A[idx + 1] = A[idx + 1], A[idx]
        idx += 2

A = [5, 3, 1, 2, 3] 
print(A)
peaks_and_valleys(A)
print(A)

A = list(range(10))
print(A)
peaks_and_valleys(A)
print(A)
