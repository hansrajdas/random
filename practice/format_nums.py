def format_nums(n, f='US'):
    s = []
    count = 0
    space = 3
    change = True
    while n:
        if count and not count % space:
            s.append(',')
            if change and f == 'Indian':
                space = 2
                change = False
                count = 0
        s.append(str(n % 10))
        n = n // 10
        count += 1
    return ''.join(reversed(s))

assert format_nums(12) == '12'
assert format_nums(123) == '123'
assert format_nums(1234) == '1,234'
assert format_nums(1234567) == '1,234,567'

assert format_nums(12, 'Indian') == '12'
assert format_nums(123, 'Indian') == '123'
assert format_nums(1234, 'Indian') == '1,234'
assert format_nums(1234567, 'Indian') == '12,34,567'
