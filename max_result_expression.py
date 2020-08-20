def prefix_exp_result(exp):
    """Evaluates prefix expression."""
    lis = exp.split(' ')
    idx = len(lis) - 1
    stack = []
    while idx >= 0:
        print(stack)
        if lis[idx].isdigit():
            stack.append(int(lis[idx]))
        else:
            if len(stack) < 2:
                return None
            o1 = stack.pop()
            o2 = stack.pop()
            if lis[idx] == '+':
                stack.append(o1 + o2)
            elif lis[idx] == '-':
                stack.append(o1 - o2)
            elif lis[idx] == '*':
                stack.append(o1 * o2)
            elif lis[idx] == '/':
                stack.append(o1 / o2)
            else:
                return None
        idx -= 1
    if len(stack) == 1:
        return stack.pop()
    else:
        return None
                
            
def max_result_expression(expression, variables):
    ex = expression.replace('x', '1')
    ex = ex.replace('y', '1')
    local_max = prefix_exp_result(ex)
    if local_max is None:
        return None  # expression not valid
    _max = 0
    if 'x' in variables:
        for x in range(variables['x'][0], variables['x'][1]):
            if 'y' in variables:
                for y in range(variables['y'][0], variables['y'][1]):
                    ex = expression.replace('x', str(x))
                    ex = ex.replace('y', str(y))
                    local_max = prefix_exp_result(ex)
                    if local_max > _max:
                        _max = local_max
            else:
                    ex = expression.replace('x', str(x))
                    local_max = prefix_exp_result(ex)
                    if local_max > _max:
                        _max = local_max
    else:
        _max = prefix_exp_result(expression)
    return _max


# assert max_result_expression('+ 1 2', {}) == 3
# assert max_result_expression('+ 1 5', {}) == 6
# assert max_result_expression('9', {}) == 9
# assert max_result_expression('* + 1 2 3', {}) == 9
# assert max_result_expression('+ 6 * - 4 + 2 3 8', {}) == -2
# assert max_result_expression('* + 2 x y', {'x': (0, 2), 'y': (2, 4)}) == 9
# assert max_result_expression('+ 10 x', {'x': (3, 7)}) == 16
# assert max_result_expression('-+1 5 3', {}) == None
assert max_result_expression('+ 1 2 3', {}) == None
