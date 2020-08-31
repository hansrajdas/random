def insertion_sort_descending(A):
    for i in range(1, len(A)):  # Fisrt element is sorted in itself
        element = A[i]
        j = i
        while j:
            if A[j - 1] > element:
                break
            A[j] = A[j - 1]
            j -= 1
        A[j] = element

def sort(A):
    B = A[:]
    insertion_sort_increasing(A)
    insertion_sort_descending(B)
    return (A, B)

assert sort([3, 4, 5, 2, 1]) == ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
assert sort([3, 4, 5, 2, 1, 6]) == ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
assert sort([]) == ([], [])
assert sort([1]) == ([1], [1])
assert sort([2, 1]) == ([1, 2], [2, 1])
