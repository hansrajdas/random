def search(A, key):
    if not A:
        return -1
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        if A[mid] == '':
            idx = mid
            while idx > left and A[idx] == '':
                idx -= 1
            if A[idx] == '' or A[idx] < key:
                left = mid + 1
            elif A[idx] > key:
                right = idx - 1
            else:
                return idx
        elif A[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1

A = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
print(search(A, 'ball'))
print(search(['ball'], 'ball'))

A = ['at', '', '', '', '', '', 'car', '', '', 'dad', '', '']
print(search(A, 'ball'))
