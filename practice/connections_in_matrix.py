def is_valid(r, c, rows, cols):
    return r >= 0 and c >= 0 and r < rows and c < cols

def get_connections(rows, cols, matrix):
    connections = 0
    for r in range(rows):
        for c in range(cols):
            if not matrix[r][c]:
                continue
            if is_valid(r + 1, c, rows, cols) and matrix[r + 1][c]:  # Lower
                connections += 1
            if is_valid(r, c + 1, rows, cols) and matrix[r][c + 1]:  # Right
                connections += 1
            if is_valid(r + 1, c + 1, rows, cols) and matrix[r + 1][c + 1]:  # Right lower
                connections += 1
            if is_valid(r - 1, c + 1, rows, cols) and matrix[r - 1][c + 1]:  # Right upper
                connections += 1
    print(connections)
    return connections


def main():
  matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 0, 1],
  ]
  assert get_connections(3, 4, matrix) == 8  # 8

  matrix = [[1, 1, 1]]
  assert get_connections(1, 3, matrix) == 2  # 2

  matrix = [
    [1],
    [0],
    [1],
  ]
  assert get_connections(3, 1, matrix) == 0  # 0

  matrix = [[1]]
  assert get_connections(1, 1, matrix) == 0  # 0

  matrix = [
    [1, 1],
    [0, 1],
  ]
  assert get_connections(2, 2, matrix) == 3  # 3


if __name__ == '__main__':
  main()
