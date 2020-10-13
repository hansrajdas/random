def is_invalid(M, n, r, c):
    return r < 0 or c < 0 or r > n - 1 or c > n - 1 or M[r][c] != 0

def spiral_matrix(n):
    M = [[0] * n for _ in range(n)]

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    v = 1
    d = 0
    r = 0
    c = 0
    while v <= n * n:
        M[r][c] = v
        v += 1
        if is_invalid(M, n, r + direction[d][0], c + direction[d][1]):
            d = (d + 1) % 4
        r += direction[d][0]
        c += direction[d][1]
    
    for r in M:
        print(r)

def create_spiral_matrix_layer(n):
    M = [[0] * n for _ in range(n)]
    v = 0

    for layer in range((n + 1) // 2):
        # Left to right
        for idx in range(layer, n - layer):
            v += 1
            M[layer][idx] = v

        # Top to down
        for idx in range(layer + 1, n - layer):
            v += 1
            M[idx][n - layer - 1] = v

        # Right to left
        for idx in range(n - layer - 2, layer - 1, -1):
            v += 1
            M[n - layer - 1][idx] = v

        # Bottom to top
        for idx in range(n - layer - 2, layer, -1):
            v += 1
            M[idx][layer] = v

    for r in M:
        print(r)
        
for i in range(9):
    print('********')
    create_spiral_matrix_layer(i)
