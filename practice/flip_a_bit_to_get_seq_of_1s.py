def max_ones(A):
    right = 0
    left = 0
    _max = 0
    while A:
        if A & 1:
            right += 1
        else:
            left = right
            right = 0
        _max = max(_max, right + left + 1)  # +1 for mid 0 to be swapped
        A >>= 1
    return _max

# 1101 1101 111
print(max_ones(1775))
print(max_ones(15))
print(max_ones(16))
print(max_ones(17))
