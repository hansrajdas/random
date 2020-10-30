def solve(exp, res, memo):
    if not len(exp):
        return 0
    if len(exp) == 1:
        return 1 if bool(exp) == res else 0
    key = exp + str(res)
    if key in memo:
        return memo[key]
    ways = 0
    for i in range(1, len(exp), 2):
        c = exp[i]
        left_expr = exp[:i]
        right_expr = exp[i + 1:]

        left_true = solve(left_expr, True, memo)
        left_false = solve(left_expr, False, memo)
        right_true = solve(right_expr, True, memo)
        right_false = solve(right_expr, False, memo)

        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if c == '&':
            total_true = left_true * right_true
        elif c == '|':
            total_true = (left_true * right_true) + (left_true * right_false) + (left_false * right_true)
        elif c == '^':
            total_true = (left_true * right_false) + (left_false * right_true)
        else:
            print('....')

        ways += total_true if res else total - total_true
    memo[key] = ways
    return ways

memo = {}
print(solve('0&1', False, memo))
print(solve('0&1', True, memo))
print(solve('0^0&0^1|1', True, memo))
print(solve('1^0|0|1', False, memo))
print(solve('0&0&0&1^1|0', True, memo))
