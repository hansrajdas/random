values = [25, 10, 5, 1]

def solve(amount, idx, dp):
    if idx >= len(values) - 1:
        return 1
    if dp[amount][idx]:
        return dp[amount][idx]
    ways = 0
    i = 0
    curr = values[idx]
    while amount >= i * curr:
        amount_remaining = amount - i * curr
        ways += solve(amount_remaining, idx + 1, dp)
        i += 1
    dp[amount][idx] = ways
    return ways

def ways(n):
    dp = [[0] * len(values) for _ in range(n + 1)]
    return solve(n, 0, dp)


print(1, ways(1))
print(ways(2))
print(ways(3))
print(ways(4))
print(5, ways(5))
print(ways(6))
print(ways(7))
print(ways(8))
print(ways(9))
print(10, ways(10))
