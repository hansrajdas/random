def solve(n):
    print('0.', end='')
    places = 32
    while True and places:
        n *= 2
        if n > 1:
            print(1, end='')
        elif n < 1:
            print(0, end='')
        else:
            print(1, end='')
            break
        places -= 1
    print()

solve(0.5)
solve(0.1)
