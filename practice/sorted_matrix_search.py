def sorted_search_matrix(M, x):
    row = 0
    col = len(M[0]) - 1
    while col >= 0 and row < len(M):
        if M[row][col] == x:
            return True
        if M[row][col] > x:
            col -= 1
        else:
            row += 1
    return False

matrix = [
                      [1,  2,  3,  10],
                      [4,  5,  6,  11],
                      [7,  8,  9,  13],
                      [12, 15, 16, 17]
                     ]

assert sorted_search_matrix(matrix, 15) == True
assert sorted_search_matrix(matrix, 17) == True
assert sorted_search_matrix(matrix, 11) == True
assert sorted_search_matrix(matrix, 12) == True
assert sorted_search_matrix(matrix, 22) == False
