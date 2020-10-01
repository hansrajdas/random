def min_dist(A, n1, n2):
    _min = len(A) - 1
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if (A[i] == n1 and A[j] == n2) or (A[j] == n1 and A[i] == n2):
                _min = min(_min, j - i)
    return _min

assert min_dist([3, 5, 2, 1, 8, 4, 3], 2, 3) == 2
