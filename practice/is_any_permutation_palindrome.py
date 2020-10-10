def solve(s):
    """Check if any permutation of given string is palindrome."""
    d = 0
    for c in s:
        d ^= 1 << ord(c)

    return False if (d - 1) & d else True

assert solve('abc') == False
assert solve('aabbbbc') == True
