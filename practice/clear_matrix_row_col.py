def clear_row_col(M):
    first_col_has_zero = False
    first_row_has_zero = False

    for r in M:
        if not r[0]:
            first_col_has_zero = True
            break

    for c in M[0]:
        if not c:
            first_row_has_zero = True

    for r in range(len(M)):
        for c in range(len(M[0])):
            if not M[r][c]:
                M[r][0] = 0
                M[0][c] = 0

    for c in range(1, len(M[0])):
        if not M[0][c]:
            clear_col(M, c)

    for r in range(1, len(M)):
        if not M[r][0]:
            clear_row(M, r)

    if first_col_has_zero:
        clear_col(M, 0)

    if first_row_has_zero:
        clear_row(M, 0)

def clear_row(M, r):
    cols = len(M[0])
    for c in range(cols):
        M[r][c] = 0

def clear_col(M, c):
    for r in range(len(M)):
        M[r][c] = 0
        

M = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],
]
clear_row_col(M)
for r in M:
    print(r)

M = [
    [1, 2, 3, 10],
    [0, 5, 6, 20],
    [7, 8, 0, 30],
    [40, 50, 60, 70],
]
clear_row_col(M)
for r in M:
    print(r)
