def rotate_matrix(M):
    n = len(M)
    n = len(M[0])

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for idx in range(first, last):
            offset = idx - first
            x = M[layer][idx]
            M[layer][idx] = M[last - offset][first]
            M[last - offset][first] = M[last][last - offset]
            M[last][last - offset] = M[idx][last]
            M[idx][last] = x





M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
rotate_matrix(M)
for r in M:
    print(r)

M = [
    [1, 2, 3, 10],
    [4, 5, 6, 20],
    [7, 8, 9, 30],
    [40, 50, 60, 70],
]
rotate_matrix(M)
for r in M:
    print(r)
