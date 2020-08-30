def bubble_sort_descending(A):
    i = 0
    while i < len(A):
        j = 1
        has_swap = False
        while j < len(A) - i:
            if A[j - 1] < A[j]:
                has_swap = True
                A[j - 1], A[j] = A[j], A[j - 1]
            j += 1
        i += 1
        if not has_swap:
            break

def sort(A):
    bubble_sort_descending(A)
    return A

assert sort([3, 4, 5, 2, 1]) == [5, 4, 3, 2, 1]
assert sort([3, 4, 5, 2, 1, 6]) == [6, 5, 4, 3, 2, 1]
assert sort([]) == []
assert sort([1]) == [1]
assert sort([2, 1]) == [2, 1]
