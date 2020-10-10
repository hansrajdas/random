def solve(s1, s2):
    d = {}
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s2:
        if c not in d:
            return False
        d[c] -= 1

    for k in d:
        if d[k] != 0:
            return False
    return True


assert solve('abc', 'cba') == True
assert solve('abc', 'dba') == False
assert solve('abc', 'abcabc') == False
