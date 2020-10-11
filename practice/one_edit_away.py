def solve(s1, s2):
    if len(s1) > len(s2):
        longer = s1
        shorter = s2
    else:
        longer = s2
        shorter = s1
    if len(longer) - len(shorter) > 1:
        return False

    l_idx = 0
    s_idx = 0
    diff_found = False
    while l_idx < len(longer) and s_idx < len(shorter):
        if longer[l_idx] != shorter[s_idx]:
            if diff_found:
                return False
            diff_found = True
            if len(longer) != len(shorter):
                l_idx += 1
        s_idx += 1
        l_idx += 1
    return True

assert solve('abc', 'abcd') == True
assert solve('abcd', 'abcd') == True
assert solve('abc', 'abcd') == True
assert solve('dabc', 'abcd') == False
assert solve('abcxyz', 'adcxyz') == True
