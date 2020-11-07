# Example:
# Input: N = 10000000000, M = 10011, i = 2, j = 6
# Output: 10001001100
def insert_bits(N, i, j, M):
    M = M << i
    all_ones = ~0
    mask = (1 << i) - 1 | all_ones < (j + 1)
    N = N & mask
    return N | M

print(bin(insert_bits(bin(10000000000), 2, 6, bin(10011))))
