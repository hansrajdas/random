def solve(n, src, dst, buf):
    if n > 0:
        solve(n - 1, src, buf, dst)
        print(f'Move disk {n} from {src} to {dst}')
        solve(n - 1, buf, dst, src)

src = 'A'
dst = 'B'
buf = 'C'

solve(0, src, dst, buf)
print()
solve(1, src, dst, buf)
print()
solve(2, src, dst, buf)
print()
solve(3, src, dst, buf)
print()
solve(4, src, dst, buf)
