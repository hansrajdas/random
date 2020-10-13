def print_matrix_in_spiral_simple(M):
    res = []
    rows = len(M)
    cols = len(M[0])
    size = rows * cols
    top = 0
    left = 0
    right = cols - 1
    bottom = rows - 1

    while len(res) < size:
        # Left to right
        for i in range(left, right + 1):
            if len(res) < size:
                res.append(M[top][i])
        top += 1

        # Top to bottom
        for i in range(top, bottom + 1):
            if len(res) < size:
                res.append(M[i][right])
        right -= 1

        # Right to left
        for i in range(right, left - 1, -1):
            if len(res) < size:
                res.append(M[bottom][i])
        bottom -= 1

        # Bottom to top
        for i in range(bottom, top - 1, -1):
            if len(res) < size:
                res.append(M[i][left])
        left += 1
    return res
            

def main():
  matrix = [
    [1, 2, 3, 13, 23],
    [4, 5, 6, 16, 26],
    [7, 8, 9, 19, 29],
  ]
  for r in matrix:
    print(r)
  spiral = print_matrix_in_spiral_simple(matrix)
  print(spiral)
  print()


if __name__ == '__main__':
  main()

