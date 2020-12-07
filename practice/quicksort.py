def partition(A, low, high):
    i = low
    j = low
    pi = A[high]
    while j < high:
        if A[j] <= pi:
            A[i], A[j] = A[j], A[i]
            i += 1
        j += 1
    A[i], A[high] = A[high], A[i]
    return i
           
def quick_sort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi - 1)
        quick_sort(A, pi + 1, high)


A = [2, 3, 1, 5, 7, 8, 4]
quick_sort(A, 0, len(A) - 1)
print(A)
A = [1, 2, 3, 4, 5, 6]
quick_sort(A, 0, len(A) - 1)
print(A)
A = [7, 6, 5, 4, 3, 2, 1]
quick_sort(A, 0, len(A) - 1)
print(A)
A = [10, 80, 30, 90, 40, 50, 70]
quick_sort(A, 0, len(A) - 1)
print(A)
