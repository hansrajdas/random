def get_equilibrium_index(A):
    _sum = sum(A)
    temp_sum = 0
    for i in range(len(A)):
        if temp_sum == _sum - temp_sum - A[i]:
            return i
        else:
            temp_sum += A[i]
    return -1


assert get_equilibrium_index([2, 3, 10, 1, 4]) == 2
assert get_equilibrium_index([4, 4, 4, 4]) == -1
