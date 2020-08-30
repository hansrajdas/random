def selection_sort_descending(A):
    for i in range(len(A)):
        max_idx = i
        for j in range(i + 1, len(A)):
            if A[max_idx] < A[j]:
                max_idx = j
        A[max_idx], A[i] = A[i], A[max_idx]

def sort(A):
    selection_sort_descending(A)
    return (list(reversed(A)), A)

assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
