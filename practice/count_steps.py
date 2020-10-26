def countWaysUtils(n, memo):
    if n < 0:
        return 0
    elif not n:
        return 1
    if n not in memo:
        memo[n] = countWaysUtils(n - 1, memo) + countWaysUtils(n - 2, memo) + countWaysUtils(n - 3, memo)
    return memo[n]

def countWays(n):
    memo = {}
    return countWaysUtils(n, memo)

def main():
  for n in range(1, 25):
    print('N = {n}, Ways = {ways}'.format(n = n, ways=countWays(n)))

if __name__ == '__main__':
  main()
