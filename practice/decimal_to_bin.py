def solve(n):
    if not n:
        return
    solve(n // 2)
    print(n % 2, end='')

solve(8)
print()
solve(7)
print()
solve(6)
print()
solve(600)
