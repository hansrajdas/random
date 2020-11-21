def max_subarray_sum(A):
    max_sum = A[0]
    running_sum = A[0]
    for a in A[1:]:
        running_sum = max(running_sum + a, a)
        if max_sum < running_sum:
            max_sum = running_sum
    return max_sum

assert max_subarray_sum([2, -8, 3, -2, 4, -10]) == 5
assert max_subarray_sum([-2, -8, -3, -2, -4, -10]) == -2
