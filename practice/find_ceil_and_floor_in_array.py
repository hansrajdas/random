# Date: 2018-11-10
#
# Description:
# Given a sorted array and an integer X, find floor and ceil of X from array.
# For example:
# A = [3, 4, 7, 8, 10], X = 5 so floor of 5 would be 4 and ceil would be 7
#
# Approach:
# First check for corner cases that is:
# - If X is smaller than first element in array
# - If X is larger than last element in array
# - If above 2 don't meet do a linear search and check if we are able to find
#   same number as X in array or just larger than X.
#
# Complexity:
# O(N)


def get_floor_ceil(A, x):
    floor = float('Inf')
    ceil = float('-Inf')
    for n in A:
        if n == x:
            return (x, x)
        elif n - x > 0:
            floor = min(floor, n)
        else:
            ceil = max(ceil, n)
    return (floor, ceil)

assert get_floor_ceil([1, 2, 3, 4, 5], 4) == (4, 4)
assert get_floor_ceil([1, 5, 3, 4, 10], 6) == (10, 5)
