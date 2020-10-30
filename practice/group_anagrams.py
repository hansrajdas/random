def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    m = {}
    for c in s1:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

    for c in s2:
        if c in m:
            m[c] -= 1
    for k in m:
        if m[k]:
            return False
    return True

def get_key(_m, s):
    for k in _m:  # 
        if are_anagrams(k, s):  # O(len of string)
            return k
    return None

def group_anagrams(strings):
    _m = {}

    for s in strings: # O(N)
        k = get_key(_m, s)
        if k is None:
            _m[s] = [s]
        else:
            _m[k].append(s)
    return _m

def main():
    s = ['abc', 'def', 'xyx', 'efd', 'cba', 'yxx', 'xyz']
    _map = group_anagrams(s)
    for k in _map:
        print(_map[k])
main()
