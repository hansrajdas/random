size = 8

def check_valid_position(columns, row, col):
    for row2 in range(row):
        r = row2
        c = columns[row2]
        
        if c == col:
            return False

        diff1 = abs(r - row)
        diff2 = abs(c - col)

        if diff1 == diff2:
            return False
    return True

def place_eight_queens(columns, results, row):
    if row == size:
        results.append(columns[:])
    else:
        for c in range(size):
            if check_valid_position(columns, row, c):
                columns[row] = c
                place_eight_queens(columns, results, row + 1)

def main():
    results = []
    columns = [None] * size
    place_eight_queens(columns, results, 0)
    for r in results:
        print()
        for row in range(size):
            print('%d, %d' % (row, r[row]), end=' ')

main()
